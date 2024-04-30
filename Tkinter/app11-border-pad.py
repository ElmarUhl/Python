from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Title")

label = Label( root,
              text="Label",
              font="Arial 20",
              bd=1,
              relief="solid",
              padx=10,
              pady=10).pack()

root.mainloop()
