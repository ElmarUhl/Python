from tkinter import *

root = Tk()

class myFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'green'

f1 = myFrame(root).pack()

root.mainloop()
