from blinkstick import blinkstick


class Stimulus:
    def __init__(self):
        self.right = blinkstick.find_by_serial("BS033074-3.0")
        self.left = blinkstick.find_by_serial("BS033014-3.0")
        
    def on(self, stimulus, color):
        if stimulus.startswith(("r", "R")):    
            for led in range(8):
                self.right.set_color(0,led,name = color)
        elif stimulus.startswith(("l", "L")):
            for led in range(8):
                self.left.set_color(0,led,name = color)
        elif stimulus.startswith(("a", "A")):
            for led in range(8):
                self.left.set_color(0,led,name = color)
                self.right.set_color(0,led,name = color)
        else:
            pass
        
    def off(self, stimulus):
        self.on(stimulus, "")
        


# how to use the class Stimulus:
# 1) create object
#led = Stimulus()

# 2) start stimulus "all", "right" or "left" with color "red", "navy", "bisque" see here: https://www.w3.org/TR/css-color-3/
#led.on("all", "maroon")

# 3) turn off "all", "right" or "left" stimulus by setting color "" or "black"
#led.off("all")

#led.stimulus_left()