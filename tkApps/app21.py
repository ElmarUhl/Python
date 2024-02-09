from tkinter import *

root = Tk()
root.title("App")

varTexto = StringVar()

def mostrarNome():
    varTexto.set("O teu nome é " + textBox1.get())

label1 = Label(root, text="O teu nome é:")
textBox1 = Entry(root)
button1 = Button(root,text="Executar", command=mostrarNome)
label2 = Label(root, textvariable=varTexto)

label1.grid()
textBox1.grid()
button1.grid()
label2.grid()


root.mainloop()