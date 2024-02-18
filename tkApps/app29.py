from tkinter import *

root = Tk()

def apresentar():
    print(valor_check.get())

valor_check = IntVar()
check = Checkbutton(root, text='Esta é uma checkbox', variable=valor_check, command=apresentar).pack()

root.mainloop()
