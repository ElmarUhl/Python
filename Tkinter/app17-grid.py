from tkinter import *

root = Tk()
#menu.geometry("500x300")
root.title("Title")

l1 = Label(root, text="Label 1",bg="red",font="Arial 20")
l2 = Label(root, text="Label 2", bg="green",font="Arial 20")
l3 = Label(root, text="Label 3", bg="blue",font="Arial 20")

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)

b1 = Button(root,text="Click 1")
b2 = Button(root,text="Click 2")
b3 = Button(root,text="Click 3")

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

root.mainloop()
