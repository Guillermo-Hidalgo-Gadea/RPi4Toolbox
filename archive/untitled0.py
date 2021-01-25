import gpiozero
import blinkstick
import time

# Maybe include a popup pinout to mark button connection
GPIOA = 6 #button A 
GPIOB = 4 #button B
GPIOF = 21 #feeder

peckdiskA = gpiozero.Button(GPIOA)
peckdiskB = gpiozero.Button(GPIOB)


LEDlist = blinkstick.blinkstick.find_all()
LED0 = LEDlist[0]
LED1 = LEDlist[1]

# define useful functions
def red(LED):
    LED.set_color(0,0,255,0,0) 
    LED.set_color(0,1,255,0,0)
    LED.set_color(0,2,255,0,0)
    LED.set_color(0,3,255,0,0)
    LED.set_color(0,4,255,0,0)
    LED.set_color(0,5,255,0,0)
    LED.set_color(0,6,255,0,0)
    LED.set_color(0,7,255,0,0)

def green(LED):
    LED.set_color(0,0,0,255,0) 
    LED.set_color(0,1,0,255,0)
    LED.set_color(0,2,0,255,0)
    LED.set_color(0,3,0,255,0)
    LED.set_color(0,4,0,255,0)
    LED.set_color(0,5,0,255,0)
    LED.set_color(0,6,0,255,0)
    LED.set_color(0,7,0,255,0)

def yellow(LED):
    LED.set_color(0,0,255,255,0) 
    LED.set_color(0,1,255,255,0)
    LED.set_color(0,2,255,255,0)
    LED.set_color(0,3,255,255,0)
    LED.set_color(0,4,255,255,0)
    LED.set_color(0,5,255,255,0)
    LED.set_color(0,6,255,255,0)
    LED.set_color(0,7,255,255,0)

def off(LED):
    LED.set_color(0,0,0,0,0) 
    LED.set_color(0,1,0,0,0)
    LED.set_color(0,2,0,0,0)
    LED.set_color(0,3,0,0,0)
    LED.set_color(0,4,0,0,0)
    LED.set_color(0,5,0,0,0)
    LED.set_color(0,6,0,0,0)
    LED.set_color(0,7,0,0,0)
    
def cascade(LED):
    LED.set_color(0,0,0,0,0) 
    time.sleep(0.2)
    LED.set_color(0,1,0,0,0)
    time.sleep(0.2)
    LED.set_color(0,2,0,0,0)
    time.sleep(0.2)
    LED.set_color(0,3,0,0,0)
    time.sleep(0.2)
    LED.set_color(0,4,0,0,0)
    time.sleep(0.2)
    LED.set_color(0,5,0,0,0)
    time.sleep(0.2)
    LED.set_color(0,6,0,0,0)
    time.sleep(0.2)
    LED.set_color(0,7,0,0,0)
    time.sleep(0.2)

### START SIGNAL
# LED blink trafficlight
# RED
red(LED0)
red(LED1)
time.sleep(1)

#Turn off
off(LED0)
off(LED1)
time.sleep(1)

# YELLOW
yellow(LED0)
yellow(LED1)
time.sleep(1)

#Turn off
off(LED0)
off(LED1)
time.sleep(1)

# GREEN
green(LED0)
green(LED1)
time.sleep(1)


#Turn off
off(LED0)
off(LED1)
time.sleep(1)


### WAIT FOR CHOICE
starttime = time.time()
try:    
    while True:
        # start LED0 green
        green(LED0)
        # start LED1 red
        red(LED1)
        
        if peckdiskB.is_pressed:
            print('Coice A')
            #Turn off
            cascade(LED1)
            
        elif peckdiskA.is_pressed:
            print('Choice B')
            cascade(LED0)
            
            
        looptime = time.time()
        if looptime - starttime > 3000:
            print('session ended') 
            #Turn off
            off(LED0)
            off(LED1)
            
            break
        
except KeyboardInterrupt:
    print('session aborted') 
    
# RED
red(LED0)
red(LED1)
time.sleep(1)

#Turn off
off(LED0)
off(LED1)
time.sleep(1)

# RED
red(LED0)
red(LED1)
time.sleep(1)

#Turn off
off(LED0)
off(LED1)
time.sleep(1)

# RED
red(LED0)
red(LED1)
time.sleep(1)

#Turn off
off(LED0)
off(LED1)
time.sleep(1)

### END TRIAL
peckdiskA.close()
peckdiskB.close()


#buttonA.when_pressed = reward_large
