from tkinter import *

menu = Tk()
menu.title("Title")
menu.geometry("500x300")

label1 = Label(menu, text="Este é o label 1",
                      bg="yellow",
                      foreground="#ff0000",
                      font="Times")

label2 = Label(menu, text="Este é o Label 2",
                    font="Arial 20 bold italic")

label3 = Label(menu, text="Este é o label 3",
                    font="Verdana 42 bold",
                    fg="#808080")
label1.pack()
label2.pack()
label3.pack()

menu.mainloop()
