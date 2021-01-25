#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:18:49 2021

@author: hidalggc
"""

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

buttonA = Button(4)
buttonB = Button(18)
camera = PiCamera()

def capture():
    timestamp = datetime.now().isoformat()
    camera.capture("/home/Desktop/%s.jpg" %timestamp)
    

buttonB.when_pressed = camera.start_preview
buttonB.when_released = camera.stop_preview
buttonA.when_pressed = capture

pause()