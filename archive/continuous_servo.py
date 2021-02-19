'''
Testing Duty Cycles in continuous rotation servo in for loop.
At 50Hz 1 is fastest forward, 18 flipping point and 98 fastest backwards 
'''
import RPi.GPIO as GPIO
import time
import os

# Part 1: testing  Duty cycles 0-100 and observe rotation speed and direction 

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
pwm = GPIO.PWM(14, 50)

pwm.start(0)

try:
    while True:
        for p in range(30):
            pwm.ChangeDutyCycle(p)
            time.sleep(2)
            print("%f " %p)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()


# Part 2: Testing Duty Cycles observed in experiment above
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
pwm = GPIO.PWM(14, 50)

pwm.start(0)
pwm.ChangeDutyCycle(1) # fastest forward
time.sleep(3)

pwm.ChangeDutyCycle(18) # flipping point
time.sleep(3)

pwm.ChangeDutyCycle(98) # fastest backwards
time.sleep(3)

pwm.ChangeDutyCycle(0) # stop
time.sleep(3)

pwm.ChangeDutyCycle(100) # stop
time.sleep(3)

pwm.stop()
GPIO.cleanup()

# Part 3: Testing sleep times given rotation speed

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
pwm = GPIO.PWM(14, 50)

pwm.start(0)

# forward speed: 1 full cycle in 3/4 seconds
pwm.ChangeDutyCycle(1) # fastest forward
time.sleep(0.85)
pwm.ChangeDutyCycle(0) # stop


# backward speed: 1 full cycle in 6/4 second
pwm.ChangeDutyCycle(98) # fastest backwards
time.sleep(1.5)
pwm.ChangeDutyCycle(0) # stop


pwm.stop()
GPIO.cleanup()

# Part 4: Testing rotatio to forward translation

# Gearwheel: 28 notches
# linear actuator: 28 notches = 9cm 
# 1 full cycle moves 9cm forward

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)


try:
    while True:
        pwm = GPIO.PWM(14, 50)
        pwm.start(1) # fastest forward
        time.sleep(0.85)
        pwm.stop()
        time.sleep(3)
                
        pwm = GPIO.PWM(14, 50)
        pwm.start(98) # fastest backwards
        time.sleep(1.5)
        pwm.stop()
        time.sleep(3)
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    
########
# ERROR so far: after setting DutyCycle(0) backwards is not working appropriately.
# in  an atempt to avoid DC(0) and using pw.stop() and re-create and start did not
# work either. Trying to export servo movement to separate file as recommended in online commenst
    
    
    
    
os.system("/home/hidalggc/Documents/RPi4Toolbox-main/archive/untitled0.py")
    
    
    
    
    
    
    
    
    
    