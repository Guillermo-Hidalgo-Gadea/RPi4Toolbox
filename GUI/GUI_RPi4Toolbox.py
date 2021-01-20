"""
Created on Tue Jan 19 15:48:01 2021

@author: Guillermo Hidalgo Gadea
"""

# GUI for RPi4 Toolbox in Kivy
import webbrowser
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Define different screens
class MainScreen(Screen):
    def homepage(self):
        webbrowser.open("https://guillermohidalgogadea.com/#contact")


class SecondScreen(Screen):
    # clear input boxes
    subject = ObjectProperty(None)
    experimenter = ObjectProperty(None)

    def clear(self):
        self.subject.text = ""
        self.experimenter.text = ""


class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class FifthScreen(Screen):
    pass

class SixthScreen(Screen):
    pass

class SeventhScreen(Screen):
    def edit(self):
        open("experimentalprotocol.yaml")

class EigthsScreen(Screen):
    def edit(self):
        open("experimentalprotocol.yaml")

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
    