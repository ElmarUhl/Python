from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class Window2(App):
    def build(self):
        return Tarefas(['Buscar filho', 'Fazer compra', 'molhar a calçada'], orientation='horizontal')
    
Window2().run()
