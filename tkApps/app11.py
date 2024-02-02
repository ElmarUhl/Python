from tkinter import *

menu = Tk()
menu.geometry("500x300")
menu.title("Title")

label = Label( menu,
              text="Label",
              font="Arial 20",
              bd=1,
              relief="solid",
              padx=10,
              pady=10).pack()

menu.mainloop()
