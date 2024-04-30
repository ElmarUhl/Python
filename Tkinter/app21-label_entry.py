from tkinter import *

def showName():
    name = text1.get()
    lF = Label(root, text="Your name is " + name).grid()

root = Tk()
root.title("APP")
root.geometry("200x100")

l1 = Label(root, text="Write your name:")
text1 = Entry(root)
b1 = Button(root, text="Run", command=showName)

l1.grid()
text1.grid()
b1.grid()

root.mainloop()
