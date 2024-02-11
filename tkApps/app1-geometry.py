# Primeiro aplicativo criado no tutorial de python3/Tkinter
# https://www.youtube.com/watch?v=6FJNA_l4WEE&list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h&index=3
# https://www.youtube.com/watch?v=6FJNA_l4WEE&list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h&index=4
 
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira App")

menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True,True)

# menu_inicial.minsize(100,100)
# menu_inicial.maxsize(600,480)

#menu_inicial.state("zoomed") # Não está funcionando
#menu_inicial.state("iconic")
#menu_inicial.iconbitmap('whatsapp.ico') Não funciona

menu_inicial.mainloop()
