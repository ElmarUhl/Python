from tkinter import *

root = Tk()

label1 = Label(root, text="This is label 1",
               bg="yellow",
               font="Arial 20",
               width=40)

label2 = Label(root, text="This is label 2",
                bg="red",
                font="Verdana 32",
                width=40)

label1.pack()
label2.pack()

root.mainloop()