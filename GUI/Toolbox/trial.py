# Trial Module 

import pigpio
import time
import datetime
import random


from Toolbox.stimulus import Stimulus
from Toolbox.params import Parameters

class Session:
    def __init__(self, subject, experimenter):
        self.subject = subject
        self.experimenter = experimenter
        self.session = 0
        self.trial = ''
        self.start_habituation = 0
        self.trial_count = 0


class Trial:
    def __init__(self, session):
        # read config files
        self.experiment = Parameters('/GUI/Toolbox/parameters.yaml').experiment
        self.hardware = Parameters('/GUI/Toolbox/parameters.yaml').hardware
        
        # set trial parameters
        self.habituation_time = self.experiment.habituation_time # in seconds
        self.repetitions_pertrial = self.experiment.repetitions_pertrial
        self.timeout_interval = self.experiment.timeout_interval
        self.optimal_stimuluscolor = self.experiment.optimal_stimuluscolor
        self.suboptimal_stimuluscolor = self.experiment.suboptimal_stimuluscolor
        self.optimal_reward = self.experiment.optimal_reward
        self.suboptimal_reward = self.experiment.suboptimal_reward

        # TODO initialize parameters for metadata
        self.subject = session.subject # taken from session class loaded before
        self.date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.session = session.session
        self.trial = session.trial
        self.repetition = 0
        self.start_habituation = session.start_habituation
        self.habituation_time # initialized above
        self.start_stimulus = 0
        self.reactiontime = 0
        self.optimal_stimulus = ''
        self.key_choice = ''
        self.reward = 0

        #random for now but pseudorandom from schedule/metadata
        self.setting = [random.choice(["left", "right"]) for rep in range(self.repetitions_pertrial)]
        
        # additional inits
        self.status = False # controls while loop 
        self.start_time = 0

        # TODO trial or session related?
        #self.condition = 
        #self.session = 
        #self.instructions = 
        
        #TODO read from real hardware.yaml
        # Switches
        self.left = 18 #left
        self.right = 4 #right
        # Servo
        self.servo = 14 
        # TODO create own class for feeder similar to Stimulus # MIN_WIDTH=500 MAX_WIDTH=2500
        # LEDs
        self.stimulus = Stimulus()
        
        # Initialize Pi
        # MAKE SURE TO INITIALIZE PIGPIO DEAMON FIRST TODO run command from python? sudo pigpiod
        self.pi = pigpio.pi()
        if not self.pi.connected:
           exit()
        
        # set pins
        self.pi.set_mode(self.left, pigpio.INPUT)
        self.pi.set_mode(self.right, pigpio.INPUT)
        self.pi.set_pull_up_down(self.left, pigpio.PUD_UP)
        self.pi.set_pull_up_down(self.right, pigpio.PUD_UP)

    def stop(self):
        # stop hardware 
        self.stimulus.off("all")
        self.cb1.cancel(), self.cb2.cancel()
        self.status = False # stops while loop
    
    def choice(self, gpio, level, tick):
        self.end_time = time.time()
        self.reactiontime = self.end_time - self.start_stimulus
        self.optimal_stimulus = self.setting[self.repetition]
        # TODO move print to kivy instead of terminal console
        print(f"reaction time: {round(self.reactiontime,4)} sec")
        print(f"choice: gpio {gpio}\n")
        
        # evaluate choice
        # TODO generalize gpio number 
        if gpio == 4 and self.setting[self.repetition] == "right": #see right/left position switch
            # optimal choice
            self.reward = self.optimal_reward
            self.key_choice = "right"
        elif gpio == 18 and self.setting[self.repetition] == "left":
            # optimal choice
            self.reward = self.optimal_reward
            self.key_choice = "left"
        else:
            # suboptimal choice
            self.reward = self.suboptimal_reward
            if self.setting[self.repetition] == "right":
                self.key_choice = "left"   
            elif self.setting[self.repetition] == "left":
                self.key_choice = "right"  

        # move feeder forward
        self.pi.set_servo_pulsewidth(self.servo, 500)
        time.sleep(0.82)
        # wait for feeding time
        self.pi.set_servo_pulsewidth(self.servo, 0)
        time.sleep(self.reward)
        # move feeder backward
        self.pi.set_servo_pulsewidth(self.servo, 2500)
        time.sleep(0.82)
        # stop servo
        self.pi.set_servo_pulsewidth(self.servo, 0)
        
        # stop trial
        self.stop()

    def start(self):
        for rep in range(self.repetitions_pertrial):
        
            # start sequence with stimulus flash
            self.stimulus.on("all", self.suboptimal_stimuluscolor)
            time.sleep(0.2)
            self.repetition = rep
            
            # set stimulus for given rep from self.setting list
            self.stimulus.on(self.setting[self.repetition], self.optimal_stimuluscolor)
            print(f"Repetition {rep}:")
            
            # activate callback for PeckKeys
            self.cb1 = self.pi.callback(self.left, pigpio.FALLING_EDGE, self.choice)
            self.cb2 = self.pi.callback(self.right, pigpio.FALLING_EDGE, self.choice)
            
            # start waiting loop
            self.start_stimulus = time.time()
            self.status = True
            
            while self.status:
                # check elapsed time in loop
                current_time = time.time()
                self.elapsed_time = current_time - self.start_stimulus
                
                # check for timeout
                if self.elapsed_time > self.timeout_interval:
                    print("timeout")
                    break

                # callbacks activated during loop, keypeck breacks loop
            
            # stop hardware 
            self.stimulus.off("all")
            self.cb1.cancel()
            self.cb2.cancel()

            # TODO save metadata to dict
        
        self.pi.stop()
        # TODO save metadata to yaml

        

#Trial().start()

    