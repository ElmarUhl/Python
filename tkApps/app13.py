from tkinter import *

menu = Tk()
menu.title("Title")
menu.geometry("500x300")

label1 = Label(
    menu,
    text= "Frase de teste",
    font="Arial 20",
    bd=1,
    relief="solid"
)
label1.pack()

label2 = Label(menu)
label2["text"]= "Frase de teste 2"
label2['font'] = "Arial 12"
label2['bd'] = 1
label2['relief'] = "solid"
label2.pack()

label2['text'] = "Novo texto"

print(label2.keys())

for item in label2.keys():
    print(item, " : ", label2[item])

menu.mainloop()
