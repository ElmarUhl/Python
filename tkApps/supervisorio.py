from tkinter import *

status = 0

def muda():
    global status
    if(status):
        status = 0
        label['text'] = "Desligado"
    else:
        status = 1
        label['text'] = "Ligado"

root = Tk()
root.configure(background='white')

img = PhotoImage(file="tkApps/Dog.png")
label = Label(root, image=img).pack()

btn = Button(root, text='ON/OFF', command=muda).pack()
label = Label(root, text="Desligado")
label.pack()

root.mainloop()