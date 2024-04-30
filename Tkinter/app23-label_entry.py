from tkinter import *

root = Tk()

final = StringVar()

t = 0
def calc():
    F = float(e1.get())
    C = (F - 32) * 5/9
    final.set(str(round(C,1)) + " Celsius degrees")
    
l1 = Label(root, text="Farenheit degrees")
e1 = Entry(root)
b1 = Button(root, text="Calculate", command=calc)
answer = Label(root, textvariable=final)

l1.grid()
e1.grid()
answer.grid()
b1.grid()

root.mainloop()
