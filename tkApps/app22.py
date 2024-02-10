from tkinter import *

def mostrarNome():
    nome = textBox1.get()
    labelFinal = Label(root, text="O teu nome é " + nome).grid()

root = Tk()
root.title("APP")
root.geometry("200x100")

label1 = Label(root, text="Escreve o teu nome:")
textBox1 = Entry(root)
button1 = Button(root, text="Executar", command=mostrarNome)

label1.grid()
textBox1.grid()
button1.grid()

root.mainloop()