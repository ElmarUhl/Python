from tkinter import *

menu = Tk()

label1 = Label(menu, text="Este é o label 1",
               bg="yellow",
               font="Arial 20",
               width=40)

label2 = Label(menu, text="Este é o label 2",
                bg="red",
                font="Verdana 32",
                width=40)

label1.pack()
label2.pack()

menu.mainloop()