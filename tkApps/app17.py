from tkinter import *

menu = Tk()
menu.title("Title")

Label(menu, width=20, bg="red").grid(column=0)
Label(menu, width=20, bg="blue").grid(column=1)
Label(menu, bg="green").grid(columnspan=2, sticky="we")

menu.mainloop()