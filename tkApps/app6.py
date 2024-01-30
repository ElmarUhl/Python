from tkinter import *

menu = Tk()
menu.title("Title")

label1 = Label(menu,text="Label 1")
label2 = Label(menu, text="Label 2")

button = Button(menu, text="Fechar", command=lambda: quit())

label1.pack()
label2.pack()
button.pack()

menu.mainloop()