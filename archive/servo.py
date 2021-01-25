#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:07:06 2020

@author: ubuntu
"""



from gpiozero import Servo
from time import sleep

feeder_pin = 14

feeder = Servo(feeder_pin) #automatically moves in 
feeder.min()

feeder.max()
sleep(0.5)
feeder.min()
sleep(0.5)
feeder.max()
sleep(0.5)
feeder.min()
sleep(0.5)
feeder.max()
sleep(0.5)

feeder.close()     

