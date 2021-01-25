#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:01:15 2020

@author: ubuntu
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
p = GPIO.PWM(14, 100)

p.start(0)



try:
        while True:
                p.ChangeDutyCycle(1)
                time.sleep(0.7)
                p.ChangeDutyCycle(0)
                time.sleep(3)
                p.ChangeDutyCycle(97)
                time.sleep(1.1)
                p.ChangeDutyCycle(0)
                time.sleep(3)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

