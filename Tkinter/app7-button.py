from tkinter import *

menu = Tk()

menu.title("Button")
menu.geometry("200x100")

def cmd_click(mensagem):
    print(mensagem)

b1 = Button(menu,text="Run", command= lambda: cmd_click("Hello"))
b1.pack()

b2 = Button(menu, text="Print", command=lambda: print("Ok"))
b2.pack()

b3 = Button(menu, text="Exit", command= lambda: quit())
b3.pack()

menu.mainloop()
