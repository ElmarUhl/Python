from tkinter import *

root = Tk()
root.geometry('300x200')

def openForm():
    #top level
    top = Toplevel()
    top.title('New Form')
    top.geometry('200x100')
    l = Label(top, text='Label on toplevel')
    l.pack()

b = Button(root, text='New...', command=openForm)
b.pack()

root.mainloop()
