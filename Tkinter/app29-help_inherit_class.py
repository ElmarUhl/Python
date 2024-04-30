from tkinter import *

root = Tk()

class myClass(Frame):
    def __init__(self, parent):
        super().__init__()
        self['bg'] = 'red'

print(help(myClass))

root.mainloop()
