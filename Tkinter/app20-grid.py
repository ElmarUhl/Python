from tkinter import *

root = Tk()
root.title("Title")

Label(root, width=20, bg="red").grid(column=0)
Label(root, width=20, bg="blue").grid(column=1)
Label(root, bg="green").grid(columnspan=2, sticky="we")

root.mainloop()