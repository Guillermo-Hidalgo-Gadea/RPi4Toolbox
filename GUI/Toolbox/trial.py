import pigpio
import time
import random

import sys
sys.path.append('/home/hidalggc/Documents/RPi4Toolbox/Toolbox')
from stimulus import Stimulus
from params import Parameters

class Trial:
    def __init__(self):
        self.experiment = Parameters('/home/hidalggc/Documents/RPi4Toolbox/Toolbox/parameters.yaml').experiment
        #self.hardware = Parameters('parameters.yaml').hardware
        #self.hardware = 
        #self.condition = 
        #self.session = 
        #self.instructions = 
        
        # Switches
        self.GPIOA = 18 #left
        self.GPIOB = 4 #right
        
        # Servo
        self.servo = 14 # MIN_WIDTH=500 MAX_WIDTH=2500
        
        # LEDs
        self.stimulus = Stimulus()
        
        # Initialize Pi
        # MAKE SURE TO INITIALIZE PIGPIO DEAMON FIRST
        # sudo pigpiod
        self.pi = pigpio.pi()
        if not self.pi.connected:
           exit()
        
        self.pi.set_mode(self.GPIOA, pigpio.INPUT)
        self.pi.set_mode(self.GPIOB, pigpio.INPUT)
        self.pi.set_pull_up_down(self.GPIOA, pigpio.PUD_UP)
        self.pi.set_pull_up_down(self.GPIOB, pigpio.PUD_UP)
        
        # habituation time
        self.habituation_time = self.experiment.habituation_time # in seconds

        
        #random for now but pseudorandom from schedule/metadata
        self.setting = [random.choice(["left", "right"]) for rep in range(self.experiment.repetitions)]
        
        # additional inits
        self.status = False
        self.counter = 0
        self.start_time = 0

    def stop(self):
        # stop hardware 
        self.stimulus.off("all")
        self.cb1.cancel(), self.cb2.cancel()
        self.status = False # stops while loop
    
    def choice(self, gpio, level, tick):
        # log choice
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"reaction time: {round(self.elapsed_time,4)} sec")
        print(f"choice: gpio {gpio}\n")
        
        # evaluate choice  
        if gpio == 4 and self.setting[self.rep] == "right": #see right/left position switch
            # optimal choice
            reward = self.experiment.optimal_reward
        elif gpio == 18 and self.setting[self.rep] == "left":
            # optimal choice
            reward = self.experiment.optimal_reward
        else:
            # suboptimal choice
            reward = self.experiment.suboptimal_reward          
        
        # move feeder forward
        self.pi.set_servo_pulsewidth(self.servo, 500)
        time.sleep(0.82)
        # wait for feeding time
        self.pi.set_servo_pulsewidth(self.servo, 0)
        time.sleep(reward)
        # move feeder backward
        self.pi.set_servo_pulsewidth(self.servo, 2500)
        time.sleep(0.82)
        # stop servo
        self.pi.set_servo_pulsewidth(self.servo, 0)
        
        # stop trial
        self.stop()

        
    def start(self):
        for rep in range(self.experiment.repetitions):
        
            # start sequence with stimulus flash
            self.stimulus.on("all", self.experiment.suboptimal_stimuluscolor)
            time.sleep(0.2)
            self.rep = rep
            
            # set stimulus for given rep from self.setting list
            self.stimulus.on(self.setting[self.rep], self.experiment.optimal_stimuluscolor)
            print(f"Repetition {rep}:")
            
            # activate callback for PeckKeys
            self.cb1 = self.pi.callback(self.GPIOA, pigpio.FALLING_EDGE, self.choice)
            self.cb2 = self.pi.callback(self.GPIOB, pigpio.FALLING_EDGE, self.choice)
            
            # start waiting loop
            self.start_time = time.time()
            self.status = True
            
            while self.status:
                current_time = time.time()
                self.elapsed_time = current_time - self.start_time
                
                # callbacks activated during loop, keypeck breacks loop
                
                if self.elapsed_time > self.experiment.timeout:
                    print("timeout")
                    break
            
            # stop hardware 
            self.stimulus.off("all")
            self.cb1.cancel()
            self.cb2.cancel()
        
        self.pi.stop()
        

#Trial().start()

    