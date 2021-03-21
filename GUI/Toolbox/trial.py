# Trial Module 

import pigpio
import time
import datetime
import random


#from Toolbox.stimulus import Stimulus
from Toolbox.params import Parameters
from Toolbox.metadata import Metadata

class Session:
    def __init__(self, subject, experimenter):
        # take attributes from manual input
        self.subject = subject
        self.experimenter = experimenter
        self.date = datetime.datetime.now().strftime('%Y-%m-%d')
        
        # TODO extract attributes from database
        # could be read from metadata, but metadata file will be getting large quickly
        # instead, metadata.yaml is exported as csv regularly and erased to start new file. 
        # Relevant info to initialize session is passed to subject database instead. 
        self.database = Parameters('/GUI/Toolbox/parameters.yaml').database
        self.experiment = Parameters('/GUI/Toolbox/parameters.yaml').experiment
        self.condition = self.database[self.subject].condition
        self.session = self.database[self.subject].session
        self.trials_persession = self.experiment[self.condition].trials_persession
        
        # TODO get instruction for session/trial
        self.instructions = ''

        # initialize empty attributes
        self.start_habituation = 0 #update attribute on created object
        self.trial_count = 0 #update attribute on created object

class Trial:
    def __init__(self, session):
        # read config files
        self.experiment = Parameters('/GUI/Toolbox/parameters.yaml').experiment
        self.hardware = Parameters('/GUI/Toolbox/parameters.yaml').hardware
        
        # get session attributes
        self.subject = session.subject
        self.experimenter = session.experimenter
        self.date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.condition = session.condition
        self.session = session.session
        self.trial = session.trial
        self.start_habituation = session.start_habituation

        # set trial parameters
        self.habituation_time = self.experiment.habituation_time # in seconds
        self.repetitions_pertrial = self.experiment.repetitions_pertrial
        self.timeout_interval = self.experiment.timeout_interval
        self.optimal_stimuluscolor = self.experiment.optimal_stimuluscolor
        self.suboptimal_stimuluscolor = self.experiment.suboptimal_stimuluscolor
        self.optimal_reward = self.experiment.optimal_reward
        self.suboptimal_reward = self.experiment.suboptimal_reward

        # initialize trial parameters for metadata
        self.repetition = 0
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

    def pass_metadata(self):
        # create metadata object
        self.metadata = Metadata()

        # dump data from trial to metadata object
        self.metadata.subject = self.subject
        self.metadata.experimenter = self.experimenter
        self.metadata.date = self.date
        self.metadata.session = self.session
        self.metadata.condition = self.condition
        self.metadata.trial = self.trial
        self.metadata.repetition = self.repetition
        self.metadata.start_habituation = self.start_habituation
        self.metadata.start_stimulus = self.start_stimulus
        self.metadata.reactiontime_keypeck = self.reactiontime
        self.metadata.optimal_stimulus = self.optimal_stimulus
        self.metadata.key_choice = self.key_choice
        self.metadata.reward = self.reward

        # update metadata with append method
        self.metadata.append()

        # save metadata
        self.metadata.save()

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

            # save data for each repetition
            self.pass_metadata()
            
        self.pi.stop()
        # TODO save metadata to yaml


#Trial().start()