# GUI for RPi4 Toolbox in Kivy
import webbrowser
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
# own modules here
from Toolbox.trial import Trial

# Define different screens
class MainScreen(Screen):
    def homepage(self):
        webbrowser.open("https://guillermohidalgogadea.com/#contact")
    # main menu screen

class SecondScreen(Screen):
    # clear input boxes
    subject = ObjectProperty(None)
    experimenter = ObjectProperty(None)

    def clear(self):
        self.subject.text = ""
        self.experimenter.text = ""
        
    # ask for subject id and experimenter
    # popup with subject info for re-id

class ThirdScreen(Screen):
    pass
 # check metadata for subject progress
 # decide on upcoming trial
 
class FourthScreen(Screen):
    pass
 # give info on trial setup

class FifthScreen(Screen):
    countdown_seconds = Trial().habituation_time
    countdown_sarted = False
        
    def update_time(self,dt):
        if self.countdown_sarted:
            self.countdown_seconds -= dt
        minutes, seconds = divmod(self.countdown_seconds, 60)
        self.ids.countdown.text = f"{int(minutes):02}:{int(seconds):02}"    
        
        if self.countdown_seconds < 0.1:
            Clock.unschedule(self.update_time)
            self.ids.countdown.text = "00:00"
            # change screen after countdown
            self.parent.current = "trial"
        
    def on_start(self):
        Clock.schedule_interval(self.update_time,0)
        
    def start_countdown(self):
        self.on_start()
        self.countdown_sarted = not self.countdown_sarted
        

class SixthScreen(Screen):
            
    def start_trial(self):
        # start repetitions
        Trial().start()

    def on_enter(self):
        self.start_trial()
        self.ids.finish.text = "Trial finished!"


# show reps print 
# save metadata for trial in log yaml

class SeventhScreen(Screen):
    def on_pre_enter(self):
        self.ids.description.text = Trial().experiment.description
    
    def edit(self):
        webbrowser.open("/home/hidalggc/Documents/RPi4Toolbox/GUI/Toolbox/experiment.yaml")

class EigthsScreen(Screen):
    def edit(self):
        webbrowser.open("/home/hidalggc/Documents/RPi4Toolbox/GUI/Toolbox/metadata.yaml")

class NinethScreen(Screen):
    pass
   
class WindowManager(ScreenManager):
    pass

# See outsourced GUI design in .kv file
kv = Builder.load_file('DesignGUI.kv')

        
class RPi4ToolboxGUI(App):
    def build(self):
        return kv

if __name__ == '__main__':
    RPi4ToolboxGUI().run()