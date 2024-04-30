from tkinter import *

root = Tk()

root.title("Title")
root.geometry("300x300")

border = 10

label1 = Label(root,
               text="This is label 1\nIt's second line of label 1",
               font="Arial 12"
               ).pack()

label1 = Label(root,
               text="flat",
               font="Arial 12",
               bd=border,
               relief="flat"
               ).pack()
label1 = Label(root,
               text="groove",
               font="Arial 12",
               bd=border,
               relief="groove"
               ).pack()
label1 = Label(root,
               text="raised",
               font="Arial 12",
               bd=border,
               relief="raised"
               ).pack()
label1 = Label(root,
               text="ridge",
               font="Arial 12",
               bd=border,
               relief="ridge"
               ).pack()
label1 = Label(root,
               text="solid",
               font="Arial 12",
               bd=border,
               relief="solid"
               ).pack()
label1 = Label(root,
               text="sunken",
               font="Arial 12",
               bd=border,
               relief="sunken"
               ).pack()

root.mainloop()
