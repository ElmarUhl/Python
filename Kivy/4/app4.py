from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Window(App):
    def build(self):
        return Incrementador()
    
Window().run ()
