# GUI for RPi4 Toolbox in Kivy
import webbrowser
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
# own modules here
from Toolbox.trial import Trial, Session

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
# name: "selection"
   
    def load_session(self):
        # access variables from SecondScreen
        self.subject = self.manager.ids.experiment.ids.subject.text
        self.experimenter = self.manager.ids.experiment.ids.experimenter.text

        # check progress for group, condition and session
        # 1) find subject in metadata
        # 2) decide on upcoming condition, session, group
        
        # Initialize Session object
        runningSession = Session(self.subject, self.experimenter)

        runningSession.start_habituation = 0
        runningSession.trial_count = 0
     
 
class FourthScreen(Screen):
# name: "instruction"
    # load session from ThirdScreen
    runningSession = self.manager.ids.experiment.ids.experimenter.text
    # give info on trial setup
    pass
 

class FifthScreen(Screen):
#name: "countdown"
    def on_enter(self):
        self.countdown_seconds = Trial().habituation_time
        self.countdown_sarted = False
        
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
        self.trial_count += 1 
        

class SixthScreen(Screen):
# name: "trial"
    def start_trial(self):
        # start repetitions
        Trial().start()

    def on_pre_enter(self):
        self.ids.finish.text = ""
        
    def on_enter(self):
        self.start_trial()
        self.ids.finish.text = "Trial " + str(self.trial_count) + " finished!"

    def check_progress(self):
        # evaluate trial counter 
        if self.trial_count > Trial().experiment.trials_persession:
            # finish session
            # popup?
            self.ids.finish.text = "Session completed!"
            self.parent.current = "progress"
        else:
            # continue with next trial
            self.parent.current = "instruction"

        
# show reps print 
# save metadata for trial in log yaml

class SeventhScreen(Screen):
    def on_pre_enter(self):
        self.ids.description.text = Trial().experiment.description
    
    def edit(self):
        webbrowser.open("/home/hidalggc/Documents/RPi4Toolbox/GUI/Toolbox/experiment.yaml")

class EigthsScreen(Screen):
# name: "progress"
    def edit(self):
        webbrowser.open("/home/hidalggc/Documents/RPi4Toolbox/GUI/Toolbox/metadata.yaml")
    
    def export(self):
        # export metadata from yaml to csv
        pass

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