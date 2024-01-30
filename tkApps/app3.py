from tkinter import *

menu = Tk()

menu.title("Título")
menu['bg'] = 'yellow'
menu.geometry("640x480")

button = Button(menu,text="Executar")
button.pack()

menu.mainloop()
