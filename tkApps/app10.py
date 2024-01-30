from tkinter import *

menu = Tk()

menu.geometry("500x300")
menu.title("Título")

label = Label(
    menu,
    text="1234567890\n1234567890",
    font="Arial 20",
    bd=1,
    relief="solid",
    width=25,
    height=4,
    anchor=CENTER
).pack()

menu.mainloop()
