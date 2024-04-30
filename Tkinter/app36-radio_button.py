from tkinter import *

root = Tk()

fA = Frame(root, bd=1, relief='solid')
fA.pack()

fB = Frame(root, bd=1, relief='solid')
fB.pack()

valueA = IntVar()
valueB = IntVar()

def option():
    print('Option 1')

ra1 = Radiobutton(fA, text='Option A 1', variable=valueA, value=1, command=option)
ra2 = Radiobutton(fA, text='Option A 2', variable=valueA, value=2, indicatoron=0)
ra3 = Radiobutton(fA, text='Option A 3', variable=valueA, value=3)

ra1.pack()
ra2.pack()
ra3.pack()

rb1 = Radiobutton(fB, text='Option B 1', variable=valueB, value=1, command=option)
rb2 = Radiobutton(fB, text='Option B 2', variable=valueB, value=2, indicatoron=0)
rb3 = Radiobutton(fB, text='Option B 3', variable=valueB, value=3)

rb1.pack()
rb2.pack()
rb3.pack()

ra2.select()

def showRadio():
    print(valueA.get())
    
cmd = Button(root, text='Click', command=showRadio)
cmd.pack()

root.mainloop()
