from tkinter import *

menu = Tk()

menu.title("Botão")
menu.geometry("600x480")

def cmd_click(mensagem):
    print(mensagem)

botao1 = Button(menu,text="Executar", command= lambda: cmd_click("Olá"))
botao1.pack()

botao2 = Button(menu, text="Print", command=lambda: print("Ok"))
botao2.pack()

botao3 = Button(menu, text="Sair", command= lambda: quit())
botao3.pack()

menu.mainloop()
