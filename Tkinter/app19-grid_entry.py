from tkinter import *

root = Tk()
root.title("Login")

Label(root, text="User:").grid(row=0, sticky=W)
Label(root, text="Password:").grid(row=1, sticky=W)

text_user = Entry(root).grid(row=0, column=1)
text_password = Entry(root).grid(row=1, column=1)

Button(root, text="Login").grid(row=2, column=1, sticky=E)

root.mainloop()