from tkinter import *

root = Tk()

root.geometry("500x300")
root.title("Title")

label = Label(
    root,
    text="1234567890\n1234567890",
    font="Arial 20",
    bd=1,
    relief="solid",
    width=25,
    height=4,
    anchor=CENTER
).pack()

root.mainloop()
