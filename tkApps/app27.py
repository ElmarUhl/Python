from tkinter import *

root = Tk()

class MinhaClasse(Frame):
    def __init__(self, parent):
        super().__init__()
        self['bg'] = 'red'

print(help(MinhaClasse))

root.mainloop()
