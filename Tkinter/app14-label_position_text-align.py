from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Title")

label1 = Label(root,
               text="This is a label 1\nIt's second line of label 1",
               bd=1,
               relief="solid",
               justify=LEFT,
               anchor=W,
               width=50).pack()

root.mainloop()
