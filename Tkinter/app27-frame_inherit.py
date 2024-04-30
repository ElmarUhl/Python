from tkinter import *

class FrameName(Frame):
    def __init__(self,myMaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID
        
        lName = Label(self, text="Name: ")
        tName = Entry(self)
        
        lName.grid(row=0, column=0)
        tName.grid(row=0, column=1)

root = Tk()
root.title("App")

fName = FrameName(root).grid()
fName2 = FrameName(root).grid()

root.mainloop()
