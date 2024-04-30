from tkinter import *

root = Tk()
root.title("Title")

label1 = Label(root,text="Label 1")
label2 = Label(root, text="Label 2")

button = Button(root, text="Close", command=lambda: quit())

label1.pack()
label2.pack()
button.pack()

root.mainloop()