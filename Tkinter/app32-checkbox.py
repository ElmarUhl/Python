from tkinter import *

root = Tk()

def show():
    if valueCheck.get():
        print('Check box checked')
    else:
        print('Check box unchecked')

valueCheck = IntVar()
check = Checkbutton(root, text='This is a checkbox', variable=valueCheck, command=show).pack()

root.mainloop()
