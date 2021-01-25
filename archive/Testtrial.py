import gpiozero
from blinkstick import blinkstick
import time

# Maybe include a popup pinout to mark button connection
GPIOA = 18 #button A 
GPIOB = 4 #button B
GPIOF = 21 #feeder

peckdiskA = gpiozero.Button(GPIOA)
peckdiskB = gpiozero.Button(GPIOB)


LEDlist = blinkstick.find_all()
LED0 = LEDlist[0]
LED1 = LEDlist[1]

# Servo correction
#myCorrection=0.8
#maxPW=(2.0+myCorrection)/1000
#minPW=(1.0-myCorrection)/1000

#feeder = gpiozero.Servo(GPIOF,min_pulse_width=minPW,max_pulse_width=maxPW)
#feeder.min()
#time.sleep(2)



### START SIGNAL
# LED blink trafficlight
# RED
LED0.set_color(0,0,255,0,0) 
LED0.set_color(0,1,255,0,0)
LED0.set_color(0,2,255,0,0)
LED0.set_color(0,3,255,0,0)
LED0.set_color(0,4,255,0,0)
LED0.set_color(0,5,255,0,0)
LED0.set_color(0,6,255,0,0)
LED0.set_color(0,7,255,0,0)

LED1.set_color(0,0,255,0,0) 
LED1.set_color(0,1,255,0,0)
LED1.set_color(0,2,255,0,0)
LED1.set_color(0,3,255,0,0)
LED1.set_color(0,4,255,0,0)
LED1.set_color(0,5,255,0,0)
LED1.set_color(0,6,255,0,0)
LED1.set_color(0,7,255,0,0)

time.sleep(1.5)

#Turn off
LED0.set_color(0,0,0,0,0) 
LED0.set_color(0,1,0,0,0)
LED0.set_color(0,2,0,0,0)
LED0.set_color(0,3,0,0,0)
LED0.set_color(0,4,0,0,0)
LED0.set_color(0,5,0,0,0)
LED0.set_color(0,6,0,0,0)
LED0.set_color(0,7,0,0,0)

LED1.set_color(0,0,0,0,0) 
LED1.set_color(0,1,0,0,0)
LED1.set_color(0,2,0,0,0)
LED1.set_color(0,3,0,0,0)
LED1.set_color(0,4,0,0,0)
LED1.set_color(0,5,0,0,0)
LED1.set_color(0,6,0,0,0)
LED1.set_color(0,7,0,0,0)

time.sleep(1)

# YELLOW
LED0.set_color(0,0,255,255,0) 
LED0.set_color(0,1,255,255,0)
LED0.set_color(0,2,255,255,0)
LED0.set_color(0,3,255,255,0)
LED0.set_color(0,4,255,255,0)
LED0.set_color(0,5,255,255,0)
LED0.set_color(0,6,255,255,0)
LED0.set_color(0,7,255,255,0)

LED1.set_color(0,0,255,255,0) 
LED1.set_color(0,1,255,255,0)
LED1.set_color(0,2,255,255,0)
LED1.set_color(0,3,255,255,0)
LED1.set_color(0,4,255,255,0)
LED1.set_color(0,5,255,255,0)
LED1.set_color(0,6,255,255,0)
LED1.set_color(0,7,255,255,0)

time.sleep(1.5)

#Turn off
LED0.set_color(0,0,0,0,0) 
LED0.set_color(0,1,0,0,0)
LED0.set_color(0,2,0,0,0)
LED0.set_color(0,3,0,0,0)
LED0.set_color(0,4,0,0,0)
LED0.set_color(0,5,0,0,0)
LED0.set_color(0,6,0,0,0)
LED0.set_color(0,7,0,0,0)

LED1.set_color(0,0,0,0,0) 
LED1.set_color(0,1,0,0,0)
LED1.set_color(0,2,0,0,0)
LED1.set_color(0,3,0,0,0)
LED1.set_color(0,4,0,0,0)
LED1.set_color(0,5,0,0,0)
LED1.set_color(0,6,0,0,0)
LED1.set_color(0,7,0,0,0)

time.sleep(1)

# GREEN
LED0.set_color(0,0,0,255,0) 
LED0.set_color(0,1,0,255,0)
LED0.set_color(0,2,0,255,0)
LED0.set_color(0,3,0,255,0)
LED0.set_color(0,4,0,255,0)
LED0.set_color(0,5,0,255,0)
LED0.set_color(0,6,0,255,0)
LED0.set_color(0,7,0,255,0)

LED1.set_color(0,0,0,255,0) 
LED1.set_color(0,1,0,255,0)
LED1.set_color(0,2,0,255,0)
LED1.set_color(0,3,0,255,0)
LED1.set_color(0,4,0,255,0)
LED1.set_color(0,5,0,255,0)
LED1.set_color(0,6,0,255,0)
LED1.set_color(0,7,0,255,0)

time.sleep(1.5)

# feeder move

#feeder.max()
#time.sleep(2)
#feeder.min()

#Turn off
LED0.set_color(0,0,0,0,0) 
LED0.set_color(0,1,0,0,0)
LED0.set_color(0,2,0,0,0)
LED0.set_color(0,3,0,0,0)
LED0.set_color(0,4,0,0,0)
LED0.set_color(0,5,0,0,0)
LED0.set_color(0,6,0,0,0)
LED0.set_color(0,7,0,0,0)

LED1.set_color(0,0,0,0,0) 
LED1.set_color(0,1,0,0,0)
LED1.set_color(0,2,0,0,0)
LED1.set_color(0,3,0,0,0)
LED1.set_color(0,4,0,0,0)
LED1.set_color(0,5,0,0,0)
LED1.set_color(0,6,0,0,0)
LED1.set_color(0,7,0,0,0)

time.sleep(1)

### ASSIGN REWARD
# Session and trial dependent assignement, see protocol
# left is high rewarded = LED0 = peckdiskA


### WAIT FOR CHOICE
starttime = time.time()
try:    
    while True:
        # start LED0 green
        LED0.set_color(0,0,0,255,0) 
        LED0.set_color(0,1,0,255,0)
        LED0.set_color(0,2,0,255,0)
        LED0.set_color(0,3,0,255,0)
        LED0.set_color(0,4,0,255,0)
        LED0.set_color(0,5,0,255,0)
        LED0.set_color(0,6,0,255,0)
        LED0.set_color(0,7,0,255,0)
        # start LED1 red
        LED1.set_color(0,0,255,0,0) 
        LED1.set_color(0,1,255,0,0)
        LED1.set_color(0,2,255,0,0)
        LED1.set_color(0,3,255,0,0)
        LED1.set_color(0,4,255,0,0)
        LED1.set_color(0,5,255,0,0)
        LED1.set_color(0,6,255,0,0)
        LED1.set_color(0,7,255,0,0)
        
        if peckdiskB.is_pressed:
            print('Coice A :)')
            #Turn off
            LED1.set_color(0,0,0,0,0) 
            time.sleep(0.2)
            LED1.set_color(0,1,0,0,0)
            time.sleep(0.2)
            LED1.set_color(0,2,0,0,0)
            time.sleep(0.2)
            LED1.set_color(0,3,0,0,0)
            time.sleep(0.2)
            LED1.set_color(0,4,0,0,0)
            time.sleep(0.2)
            LED1.set_color(0,5,0,0,0)
            time.sleep(0.2)
            LED1.set_color(0,6,0,0,0)
            time.sleep(0.2)
            LED1.set_color(0,7,0,0,0)
            time.sleep(0.2)
            #Reward
            #feeder.min()
            #feeder.max()
            #time.sleep(3)
            #feeder.min()
            #Turn off
            LED0.set_color(0,0,0,255,0) 
            time.sleep(0.2)
            LED0.set_color(0,1,0,255,0)
            time.sleep(0.2)
            LED0.set_color(0,2,0,255,0)
            time.sleep(0.2)
            LED0.set_color(0,3,0,255,0)
            time.sleep(0.2)
            LED0.set_color(0,4,0,255,0)
            time.sleep(0.2)
            LED0.set_color(0,5,0,255,0)
            time.sleep(0.2)
            LED0.set_color(0,6,0,255,0)
            time.sleep(0.2)
            LED0.set_color(0,7,0,255,0)
            time.sleep(0.2)
            
        elif peckdiskA.is_pressed:
            print('Choice B :(')
            LED0.set_color(0,0,0,0,0) 
            time.sleep(0.2)
            LED0.set_color(0,1,0,0,0)
            time.sleep(0.2)
            LED0.set_color(0,2,0,0,0)
            time.sleep(0.2)
            LED0.set_color(0,3,0,0,0)
            time.sleep(0.2)
            LED0.set_color(0,4,0,0,0)
            time.sleep(0.2)
            LED0.set_color(0,5,0,0,0)
            time.sleep(0.2)
            LED0.set_color(0,6,0,0,0)
            time.sleep(0.2)
            LED0.set_color(0,7,0,0,0)
            time.sleep(0.2)
            
            #feeder.max()
            #time.sleep(1)
            #feeder.min()
            #Turn off
            LED1.set_color(0,0,255,0,0) 
            time.sleep(0.2)
            LED1.set_color(0,1,255,0,0)
            time.sleep(0.2)
            LED1.set_color(0,2,255,0,0)
            time.sleep(0.2)
            LED1.set_color(0,3,255,0,0)
            time.sleep(0.2)
            LED1.set_color(0,4,255,0,0)
            time.sleep(0.2)
            LED1.set_color(0,5,255,0,0)
            time.sleep(0.2)
            LED1.set_color(0,6,255,0,0)
            time.sleep(0.2)
            LED1.set_color(0,7,255,0,0)
            
            
        looptime = time.time()
        if looptime - starttime > 3000:
            print('session ended') 
            #Turn off
            LED0.set_color(0,0,0,0,0) 
            LED0.set_color(0,1,0,0,0)
            LED0.set_color(0,2,0,0,0)
            LED0.set_color(0,3,0,0,0)
            LED0.set_color(0,4,0,0,0)
            LED0.set_color(0,5,0,0,0)
            LED0.set_color(0,6,0,0,0)
            LED0.set_color(0,7,0,0,0)
            
            LED1.set_color(0,0,0,0,0) 
            LED1.set_color(0,1,0,0,0)
            LED1.set_color(0,2,0,0,0)
            LED1.set_color(0,3,0,0,0)
            LED1.set_color(0,4,0,0,0)
            LED1.set_color(0,5,0,0,0)
            LED1.set_color(0,6,0,0,0)
            LED1.set_color(0,7,0,0,0)
            break
        
        # Between Trials Interval
        time.sleep(3)
        
except KeyboardInterrupt:
    print('session aborted') 
    
# RED
LED0.set_color(0,0,255,0,0) 
LED0.set_color(0,1,255,0,0)
LED0.set_color(0,2,255,0,0)
LED0.set_color(0,3,255,0,0)
LED0.set_color(0,4,255,0,0)
LED0.set_color(0,5,255,0,0)
LED0.set_color(0,6,255,0,0)
LED0.set_color(0,7,255,0,0)

LED1.set_color(0,0,255,0,0) 
LED1.set_color(0,1,255,0,0)
LED1.set_color(0,2,255,0,0)
LED1.set_color(0,3,255,0,0)
LED1.set_color(0,4,255,0,0)
LED1.set_color(0,5,255,0,0)
LED1.set_color(0,6,255,0,0)
LED1.set_color(0,7,255,0,0)

time.sleep(1.5)

#Turn off
LED0.set_color(0,0,0,0,0) 
LED0.set_color(0,1,0,0,0)
LED0.set_color(0,2,0,0,0)
LED0.set_color(0,3,0,0,0)
LED0.set_color(0,4,0,0,0)
LED0.set_color(0,5,0,0,0)
LED0.set_color(0,6,0,0,0)
LED0.set_color(0,7,0,0,0)

LED1.set_color(0,0,0,0,0) 
LED1.set_color(0,1,0,0,0)
LED1.set_color(0,2,0,0,0)
LED1.set_color(0,3,0,0,0)
LED1.set_color(0,4,0,0,0)
LED1.set_color(0,5,0,0,0)
LED1.set_color(0,6,0,0,0)
LED1.set_color(0,7,0,0,0)

time.sleep(1)
# RED
LED0.set_color(0,0,255,0,0) 
LED0.set_color(0,1,255,0,0)
LED0.set_color(0,2,255,0,0)
LED0.set_color(0,3,255,0,0)
LED0.set_color(0,4,255,0,0)
LED0.set_color(0,5,255,0,0)
LED0.set_color(0,6,255,0,0)
LED0.set_color(0,7,255,0,0)

LED1.set_color(0,0,255,0,0) 
LED1.set_color(0,1,255,0,0)
LED1.set_color(0,2,255,0,0)
LED1.set_color(0,3,255,0,0)
LED1.set_color(0,4,255,0,0)
LED1.set_color(0,5,255,0,0)
LED1.set_color(0,6,255,0,0)
LED1.set_color(0,7,255,0,0)

time.sleep(1.5)

### END TRIAL
peckdiskA.close()
peckdiskB.close()
#feeder.close()   
#Turn off
LED0.set_color(0,0,0,0,0) 
LED0.set_color(0,1,0,0,0)
LED0.set_color(0,2,0,0,0)
LED0.set_color(0,3,0,0,0)
LED0.set_color(0,4,0,0,0)
LED0.set_color(0,5,0,0,0)
LED0.set_color(0,6,0,0,0)
LED0.set_color(0,7,0,0,0)
    
LED1.set_color(0,0,0,0,0) 
LED1.set_color(0,1,0,0,0)
LED1.set_color(0,2,0,0,0)
LED1.set_color(0,3,0,0,0)
LED1.set_color(0,4,0,0,0)
LED1.set_color(0,5,0,0,0)
LED1.set_color(0,6,0,0,0)
LED1.set_color(0,7,0,0,0)


