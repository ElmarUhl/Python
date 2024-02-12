from tkinter import *

root = Tk()

class MinhaFrame(Frame):
    def __init__(self,parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'green'

frame1 = MinhaFrame(root).pack()

root.mainloop()
