from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from blinkstick import blinkstick
from time import sleep
from queue import Queue

# Maybe include a popup pinout to mark button connection
GPIOA = 18 #button A 
GPIOB = 4 #button B

peckKeyA = Button(GPIOA)
peckKeyB = Button(GPIOB)


LEDlist = blinkstick.find_all()
LED0 = LEDlist[0]
LED1 = LEDlist[1]

camera = PiCamera()

def info():
    for bstick in blinkstick.find_all():
        print ("Found device:")
        print ("    Manufacturer:  " + bstick.get_manufacturer())
        print ("    Description:   " + bstick.get_description())
        print ("    Serial:        " + bstick.get_serial())
        print ("    Current Color: " + bstick.get_color(color_format="hex"))

def capture():
    timestamp = datetime.now().isoformat()
    camera.capture("/home/Desktop/%s.jpg" %timestamp)
    

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
    red(LED0)
    red(LED1)
    sleep(1)
    off(LED0)
    off(LED1)
    sleep(0.5)
    
    yellow(LED0)
    yellow(LED1)
    sleep(1)
    off(LED0)
    off(LED1)
    sleep(0.5)
    
    white(LED0)
    white(LED1)
    sleep(1)
    off(LED0)
    off(LED1)
    sleep(0.5)
    
def wait_button():
    queue = Queue()
    peckKeyA.when_pressed = queue.put
    peckKeyB.when_pressed = queue.put
    e = queue.get()
    if e.pin.number == GPIOA:
        choice = "peckKeyA"
    elif e.pin.number == GPIOB:
        choice = "peckKeyB"
    return choice


# start sequence
start()

try: 
    while True:
        
        # choose random trial
        red(LED0)
        green(LED1)
        
        # wait for press
        choice = wait_button()
        
        # evaluate choice
        if choice == "peckKeyB":
            print("5€ reward")
        else: 
            print("10€ reward")
        
        capture()
        
        off(LED0)
        off(LED1)
                
        sleep(1.5)

except KeyboardInterrupt:
    print("manually aborted")

# stop hardware 
off(LED0)
off(LED1)
peckKeyA.close()
peckKeyB.close()
    

    