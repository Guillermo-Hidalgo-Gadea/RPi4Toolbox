from blinkstick import blinkstick

class LED:
    def __init__(self):

        LEDlist = blinkstick.find_all()
        self.LED1 = LEDlist[0]
        self.LED2 = LEDlist[1]
        
    def on(self):
        self.LED1.set_color(0,0,255,0,0) 
        self.LED1.set_color(0,1,255,0,0)
        self.LED1.set_color(0,2,255,0,0)
        self.LED1.set_color(0,3,255,0,0)
        self.LED1.set_color(0,4,255,0,0)
        self.LED1.set_color(0,5,255,0,0)
        self.LED1.set_color(0,6,255,0,0)
        self.LED1.set_color(0,7,255,0,0)
        
        self.LED2.set_color(0,0,255,0,0) 
        self.LED2.set_color(0,1,255,0,0)
        self.LED2.set_color(0,2,255,0,0)
        self.LED2.set_color(0,3,255,0,0)
        self.LED2.set_color(0,4,255,0,0)
        self.LED2.set_color(0,5,255,0,0)
        self.LED2.set_color(0,6,255,0,0)
        self.LED2.set_color(0,7,255,0,0)
        
    def off(self):
        self.LED1.set_color(0,0,0,0,0) 
        self.LED1.set_color(0,1,0,0,0)
        self.LED1.set_color(0,2,0,0,0)
        self.LED1.set_color(0,3,0,0,0)
        self.LED1.set_color(0,4,0,0,0)
        self.LED1.set_color(0,5,0,0,0)
        self.LED1.set_color(0,6,0,0,0)
        self.LED1.set_color(0,7,0,0,0)
        
        self.LED2.set_color(0,0,0,0,0) 
        self.LED2.set_color(0,1,0,0,0)
        self.LED2.set_color(0,2,0,0,0)
        self.LED2.set_color(0,3,0,0,0)
        self.LED2.set_color(0,4,0,0,0)
        self.LED2.set_color(0,5,0,0,0)
        self.LED2.set_color(0,6,0,0,0)
        self.LED2.set_color(0,7,0,0,0)
