from tkinter import *

menu = Tk()

menu.title("Titulo")
menu.geometry("300x300")

border = 10

label1 = Label(menu,
               text="Este é o label 1\nEsta é a segunda linha do label 1",
               font="Arial 12"
               ).pack()

label1 = Label(menu,
               text="flat",
               font="Arial 12",
               bd=border,
               relief="flat"
               ).pack()
label1 = Label(menu,
               text="groove",
               font="Arial 12",
               bd=border,
               relief="groove"
               ).pack()
label1 = Label(menu,
               text="raised",
               font="Arial 12",
               bd=border,
               relief="raised"
               ).pack()
label1 = Label(menu,
               text="ridge",
               font="Arial 12",
               bd=border,
               relief="ridge"
               ).pack()
label1 = Label(menu,
               text="solid",
               font="Arial 12",
               bd=border,
               relief="solid"
               ).pack()
label1 = Label(menu,
               text="sunken",
               font="Arial 12",
               bd=border,
               relief="sunken"
               ).pack()

menu.mainloop()
