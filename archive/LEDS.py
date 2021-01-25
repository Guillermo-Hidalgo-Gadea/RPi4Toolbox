from blinkstick import blinkstick
from time import sleep

#Find the first BlinkStick
LEDlist = blinkstick.find_all()
LED0 = LEDlist[0]
LED1 = LEDlist[1]

blinkstick.get_blinkstick_package_version()


#Use R, G and B channels to control single RGB LED

#bstick = blinkstick.find_by_serial("BS000001-1.0")


# channel is color 0 -red, 1 -green, 2 -blue
# index is LED (see https://github.com/arvydas/blinkstick-python/wiki/BlinkStick-Pro%3A-Change-Color-of-a-Single-LED)


#(x, led, red, green, blue)
LED0.set_color(0,0,0,0,255)
sleep(0.5)
LED0.set_color(0,1,0,85,255)
sleep(0.5)
LED0.set_color(0,2,0,170,255)
sleep(0.5)
LED0.set_color(0,3,0,255,255)
sleep(0.5)
LED0.set_color(0,4,85,0,255)
sleep(0.5)
LED0.set_color(0,5,85,85,255)
sleep(0.5)
LED0.set_color(0,6,85,170,255)
sleep(0.5)
LED0.set_color(0,7,85,255,255)

#(x, led, red, green, blue)
LED1.set_color(0,7,255,0,0)
sleep(0.1)
LED1.set_color(0,6,255,0,0)
sleep(0.1)
LED1.set_color(0,5,255,0,0)
sleep(0.1)
LED1.set_color(0,4,255,0,0)
sleep(0.1)
LED1.set_color(0,3,255,0,0)
sleep(0.1)
LED1.set_color(0,2,255,0,0)
sleep(0.1)
LED1.set_color(0,1,255,0,0)
sleep(0.1)
LED1.set_color(0,0,255,0,0)

#Turn off
LED0.set_color(0,0,0,0,0) 
LED0.set_color(0,1,0,0,0)
LED0.set_color(0,2,0,0,0)
LED0.set_color(0,3,0,0,0)
LED0.set_color(0,4,0,0,0)
LED0.set_color(0,5,0,0,0)
LED0.set_color(0,6,0,0,0)
LED0.set_color(0,7,0,0,0)

#Turn off
LED1.set_color(0,0,0,0,0) 
LED1.set_color(0,1,0,0,0)
LED1.set_color(0,2,0,0,0)
LED1.set_color(0,3,0,0,0)
LED1.set_color(0,4,0,0,0)
LED1.set_color(0,5,0,0,0)
LED1.set_color(0,6,0,0,0)
LED1.set_color(0,7,0,0,0)

sleep(0.5)

for i in range(5):
    
    LED0.set_color(0,0,0,0,255)
    LED0.set_color(0,1,0,0,255)
    LED0.set_color(0,2,0,0,255)
    LED0.set_color(0,3,0,0,255)
    LED0.set_color(0,4,0,0,255)
    LED0.set_color(0,5,0,0,255)
    LED0.set_color(0,6,0,0,255)
    LED0.set_color(0,7,0,0,255)
    
    LED1.set_color(0,7,255,0,0)
    LED1.set_color(0,6,255,0,0)
    LED1.set_color(0,5,255,0,0)
    LED1.set_color(0,4,255,0,0)
    LED1.set_color(0,3,255,0,0)
    LED1.set_color(0,2,255,0,0)
    LED1.set_color(0,1,255,0,0)
    LED1.set_color(0,0,255,0,0)
    
    sleep(0.5)
    
    #Turn off
    LED0.set_color(0,0,0,0,0) 
    LED0.set_color(0,1,0,0,0)
    LED0.set_color(0,2,0,0,0)
    LED0.set_color(0,3,0,0,0)
    LED0.set_color(0,4,0,0,0)
    LED0.set_color(0,5,0,0,0)
    LED0.set_color(0,6,0,0,0)
    LED0.set_color(0,7,0,0,0)
    
    #Turn off
    LED1.set_color(0,0,0,0,0) 
    LED1.set_color(0,1,0,0,0)
    LED1.set_color(0,2,0,0,0)
    LED1.set_color(0,3,0,0,0)
    LED1.set_color(0,4,0,0,0)
    LED1.set_color(0,5,0,0,0)
    LED1.set_color(0,6,0,0,0)
    LED1.set_color(0,7,0,0,0)
    
    sleep(0.5)
    i+1


#LED1.pulse(name="blue")
#LED1.pulse()