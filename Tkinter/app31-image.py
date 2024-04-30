from tkinter import *

root = Tk()

img = PhotoImage(file='images/Dog.png')
l = Label(root,image=img)
l.pack()

root.mainloop()
