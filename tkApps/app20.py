from tkinter import *

root = Tk()

final = StringVar()

t = 0
def calcular():
    F = float(textBox1.get())
    C = (F - 32) * 5/9
    final.set(str(round(C,1)) + " graus Celsius")
    
label1 = Label(root, text="Graus Farenheit")
textBox1 = Entry(root)
button1 = Button(root, text="Calcular", command=calcular)
labelResultado = Label(root, textvariable=final)

label1.grid()
textBox1.grid()
labelResultado.grid()
button1.grid()

root.mainloop()
