from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Title")

t = StringVar()
t.set("Text inside variable")

l1 = Label(
    root,
    font="Arial 20",
    bg="red",
    fg = "white",
    textvariable=t
)

l1.pack()

root.mainloop()
