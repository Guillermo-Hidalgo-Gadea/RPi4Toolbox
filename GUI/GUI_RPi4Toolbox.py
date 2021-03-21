# GUI for RPi4 Toolbox in Kivy
import webbrowser
import os
from pathlib import Path
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from Toolbox.trial import Session, Trial
from Toolbox.metadata import export

# Define different screens
class MainScreen(Screen):
    def homepage(self):
        webbrowser.open("https://guillermohidalgogadea.com/#contact")
    # main menu screen

class SecondScreen(Screen):
# name:"experiment"

    # initialize empty text input
    subject = ObjectProperty(None)
    experimenter = ObjectProperty(None)

    def on_enter(self):
        self.subject.text = ''
        self.experimenter.text = ''
        
    # ask for subject id and experimenter
    def start_session(self):
        print('Subject: ', self.subject.text,' Experimenter: ', self.experimenter.text)

    # popup with subject info for re-id

class ThirdScreen(Screen):
# name: "selection"

   # update text subject progress
    def on_enter(self):
        # load running session
        running_session = Session(self.manager.ids.experiment.ids.subject.text, self.manager.ids.experiment.ids.experimenter.text)
        print('Subject: ',running_session.subject)
        print('Experimenter: ',running_session.experimenter)
        print('Session: ',running_session.session)

        #runningSession.start_habituation = 0
        #runningSession.trial_count = 0
     
 
class FourthScreen(Screen):
# name: "instruction"
    # load session from ThirdScreen
    #runningSession = self.manager.ids.experiment.ids.experimenter.text
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
        base_path = Path().parent
        file_path = (base_path / "../RPi4Toolbox/GUI/Toolbox/experiment.yaml").resolve()
        webbrowser.open(str(file_path))

class EigthsScreen(Screen):
# name: "progress"
    def edit(self):
        base_path = Path().parent
        file_path = (base_path / "../RPi4Toolbox/GUI/Toolbox/metadata.yaml").resolve()
        webbrowser.open(str(file_path))
    
    # TODO create button
    def export_metadata(self):
        # export metadata from yaml to csv
        export()
        

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