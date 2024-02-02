from tkinter import *

menu = Tk()
menu.geometry("500x300")
menu.title("Title")

texto = StringVar()
texto.set("texto na variavel")

label1 = Label(
    menu,
    font="Arial 20",
    bg="red",
    fg = "white",
    textvariable=texto
)

label1.pack()

menu.mainloop()
