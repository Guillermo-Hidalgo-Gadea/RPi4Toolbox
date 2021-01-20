"""
Created on Tue Jan 19 15:48:01 2021

@author: Guillermo Hidalgo Gadea
"""

# GUI for RPi4 Toolbox in Kivy
#import webbrowser
from kivy.app import App
#from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Define different screens
class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


# See outsourced GUI design in .kv file
kv = Builder.load_file('RPi4ToolboxScreens.kv')
#kv = Builder.load_file('new.kv')
    
#subject = ObjectProperty(None)
#experimenter = ObjectProperty(None)
    
#def press(self):
#    subject = self.subject.text
#    experimenter = self.experimenter.text
        
        # Print to console
#    print(f'Hello {experimenter}, start testing {subject}') 
        # Print to screen
        #self.add_widget(Label(text=f'Hello {experimenter}, start testing {subject}'))
        
        # clear input boxes
#    self.subject.text = ""
#    self.experimenter.text = ""
        
#def clear(self):
        # clear input boxes
#    self.subject.text = ""
#    self.experimenter.text = ""
        
        
#def callhelp(self):
#     webbrowser.open("https://guillermohidalgogadea.com/#contact")
    
#def homepage(self):
#     webbrowser.open("https://guillermohidalgogadea.com")

        
class RPi4ToolboxScreens(App):
    def build(self):
        return kv

if __name__ == '__main__':
    RPi4ToolboxScreens().run()
    