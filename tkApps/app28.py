from tkinter import *

root = Tk()

img = PhotoImage(file='Dog.png')
label = Label(root,image=img)
label.pack()

root.mainloop()
