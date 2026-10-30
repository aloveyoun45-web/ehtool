from kivy.app import App
from kivy.uix.label import Label

class EHTool(App):
    def build(self):
        return Label(text="EH TOOL Ready!")

EHTool().run()
