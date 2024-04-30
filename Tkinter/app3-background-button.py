from tkinter import *
import time
from random import randint

#def changeColor():
#    i = randint(0, 6)
#    cores = ['black', 'blue', 'yellow', 'red', 'green', 'white']
#    menu['bg'] = cores[i]


# Programa principal
menu = Tk()

menu.title("Title")
menu.geometry("640x480")

#changeColor()
menu['bg'] = 'yellow' # background color
    
button = Button(menu,text="Run", command=changeColor)
button.pack()

menu.mainloop()
