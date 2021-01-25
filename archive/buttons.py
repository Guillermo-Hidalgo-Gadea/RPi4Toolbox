# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from gpiozero import Button
from gpiozero import Servo
from blinkstick import blinkstick
from signal import pause
from time import sleep

buttonA = Button(6) # see pinnout in gpiozero documentation
LEDlist = blinkstick.find_all()
LED0 = LEDlist[0]

def reward_large():
    print("feeder for long time")
    LED0.set_color(0,0,0,0,255)
    sleep(0.5)
    LED0.set_color(0,1,0,0,255)
    sleep(0.5)
    LED0.set_color(0,2,0,0,255)
    sleep(0.5)
    LED0.set_color(0,3,0,0,255)
    sleep(0.5)
    LED0.set_color(0,4,0,0,255)
    sleep(0.5)
    LED0.set_color(0,5,0,0,255)
    sleep(0.5)
    LED0.set_color(0,6,0,0,255)
    sleep(0.5)
    LED0.set_color(0,7,0,0,255)
    LED0.set_color(0,0,0,0,0)
    sleep(0.5)
    LED0.set_color(0,1,0,0,0)
    sleep(0.5)
    LED0.set_color(0,2,0,0,0)
    sleep(0.5)
    LED0.set_color(0,3,0,0,0)
    sleep(0.5)
    LED0.set_color(0,4,0,0,0)
    sleep(0.5)
    LED0.set_color(0,5,0,0,0)
    sleep(0.5)
    LED0.set_color(0,6,0,0,0)
    sleep(0.5)
    LED0.set_color(0,7,0,0,0)

def reward_small():
    print("feeder for short time")

try:
    buttonA.when_pressed = reward_large
    pause()

except KeyboardInterrupt:
    print('session aborted') 
#while True:
#    if buttonA.is_pressed:
#        print("Button is pressed")
#    else:
#        print("Button is not pressed")
        
#
#print("Button pressed")

buttonA.close()     


    