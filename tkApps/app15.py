from tkinter import *

menu = Tk()
#menu.geometry("500x300")
menu.title("Title")

label1 = Label(menu, text="Label 1",bg="red",font="Arial 20")
label2 = Label(menu, text="Label 2", bg="green",font="Arial 20")
label3 = Label(menu, text="Label 3", bg="blue",font="Arial 20")

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)

button1 = Button(menu,text="Click 1")
button2 = Button(menu,text="Click 2")
button3 = Button(menu,text="Click 3")

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

menu.mainloop()
