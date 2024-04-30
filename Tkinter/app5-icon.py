from tkinter import *
from tkinter.ttk import *

# programa de icones não funciona no linux por enquanto
# possivelmente o gerenciador de janelas não utiliza ícones

menu_initial = Tk()
menu_initial.title("First App")

menu_initial.geometry("500x250+200+200")
menu_initial.resizable(True,True)

#menu_initial.state("zoomed")
#menu_initial.state("iconic")
#menu_initial.iconbitmap("images/whatsapp.ico") # Só funciona em ambiente windows
img = PhotoImage(file = 'images/whatsapp.png')
#menu_initial.call('wm','iconphoto', menu_initial._w, img)
#menu_initial.iconphoto(False, 'images/dog.png')
menu_initial.iconbitmap('images/whatsapp.png')

menu_initial.mainloop()
