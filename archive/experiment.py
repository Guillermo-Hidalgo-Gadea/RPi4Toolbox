from blinkstick import blinkstick
import pigpio
import time

class Experiment: 
    pass
class Session:
    pass

class Trial:
    def __init__(self):
        
    def initialize():
    
    def start():
        # for loop (max trials)
        #  if first trial
        #    long habitution
        #  elif each sixsth 
        #    short habituation
        #  else: no break
        
        # start stimulus and feeder
        # wait choice
        # reward choice
        # save metadata
        # update counter
        
    def end():
        
    
# Initialize Pi
pi = pigpio.pi()
if not pi.connected:
   exit()

# Initialize switches
GPIOA = 18
GPIOB = 4

pi.set_mode(GPIOA, pigpio.INPUT)
pi.set_mode(GPIOB, pigpio.INPUT)
pi.set_pull_up_down(GPIOA, pigpio.PUD_UP)
pi.set_pull_up_down(GPIOB, pigpio.PUD_UP)

# Initialize LEDs 
LEDlist = blinkstick.find_all()
LED0 = LEDlist[0]
LED1 = LEDlist[1]

# Initialize Servo
servo = 14 

MIN_WIDTH=500
MAX_WIDTH=2500


# Start misc functions

def trial_setting():
    '''
    Read trial settings from experimental protocol to assign optimal reward [1]
    to peckKey A or B
    '''
    settings = {0: "A", 1:"B"}
    return settings
    
def reward_time(choice):
    '''
    This function defines the feeding time in seconds for the optimal 
    and suboptimal reward, please change here 
    '''
    optimal = 4     # in seconds
    suboptimal = 1  # in seconds
    
    if choice == 0:
        reward = suboptimal # obviously needs to be adapted for the given trial
    else:
        reward = optimal
    
    return reward


def feeder(choice):
    '''
    This functions reads the reward time for the specific choice and 
    controls the servo for feeding reward
    '''
    # choose reward for given choice
    reward = reward_time(choice)
    # move feeder forward
    pi.set_servo_pulsewidth(servo, 500)
    time.sleep(0.82)
    # wait for feeding time
    pi.set_servo_pulsewidth(servo, 0)
    time.sleep(reward)
    # move feeder backward
    pi.set_servo_pulsewidth(servo, 2500)
    time.sleep(0.82)
    # stop servo
    pi.set_servo_pulsewidth(servo, 0)
    
        
def info():
    for bstick in blinkstick.find_all():
        print ("Found device:")
        print ("    Manufacturer:  " + bstick.get_manufacturer())
        print ("    Description:   " + bstick.get_description())
        print ("    Serial:        " + bstick.get_serial())
        print ("    Current Color: " + bstick.get_color(color_format="hex"))

def off(LED):
    for led in range(8):
        LED.set_color(0,led,0,0,0)
        
def red(LED):
    for led in range(8):
        LED.set_color(0,led,255,0,0)

def green(LED):
    for led in range(8):
        LED.set_color(0,led,0,255,0)

def blue(LED):
    for led in range(8):
        LED.set_color(0,led,0,0,255)

def yellow(LED):
    for led in range(8):
        LED.set_color(0,led,255,200,0)
        
def white(LED):
    for led in range(8):
        LED.set_color(0,led,255,255,255)

def start():
    red(LED0), red(LED1), time.sleep(1)
    off(LED0), off(LED1), time.sleep(0.5)
    
    yellow(LED0), yellow(LED1), time.sleep(1)
    off(LED0), off(LED1), time.sleep(0.5)
    
    white(LED0), white(LED1), time.sleep(1)
    off(LED0), off(LED1), time.sleep(0.5)

def choice(gpio, level, tick):
    # log choice
    print("%d" %gpio)
    # evaluate choice
    if gpio == 4:
        choice = 0 # suboptimal
    elif gpio == 18:
        choice = 1 # optimal
    # change choice status

    # dispense reward
    feeder(choice)
    # stop trial
    off(LED0)
    off(LED1)

# start sequence
start()

# activate callback for PeckKeys
cb1 = pi.callback(GPIOA, pigpio.FALLING_EDGE, choice)
cb2 = pi.callback(GPIOB, pigpio.FALLING_EDGE, choice)

# start trial
settings = trial_setting() # choose trial settings
red(LED0), green(LED1)
start_time = time.time()

max_time = 300 # 5 min max trial time

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > max_time:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break
    
end_time = time.time()
# stop hardware 
off(LED0), off(LED1)
cb1.cancel(), cb2.cancel()
pi.stop()

    