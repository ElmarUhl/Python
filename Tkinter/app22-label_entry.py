from tkinter import *

root = Tk()
root.title("App")

varText = StringVar()

def showName():
    varText.set("Your name is " + text1.get())

l1 = Label(root, text="Your name is ")
text1 = Entry(root)
b1 = Button(root,text="Run", command=showName)
l2 = Label(root, textvariable=varText)

l1.grid()
text1.grid()
b1.grid()
l2.grid()

root.mainloop()
