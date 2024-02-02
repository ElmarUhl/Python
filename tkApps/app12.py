from tkinter import *

menu = Tk()
menu.geometry("500x300")
menu.title("Title")

label1 = Label(menu,
               text="Este é o label1\nSegunda linha do label 1",
               bd=1,
               relief="solid",
               justify=LEFT,
               anchor=W,
               width=50).pack()

menu.mainloop()
