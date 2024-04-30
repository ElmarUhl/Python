from tkinter import *

root = Tk()
root.title("Title")
root.geometry("500x150")

label1 = Label(root, text="This is label 1",
                      bg="yellow",
                      foreground="#ff0000",
                      font="Times")

label2 = Label(root, text="This is Label 2",
                    font="Arial 20 bold italic")

label3 = Label(root, text="This is Label 3",
                    font="Verdana 42 bold",
                    fg="#808080")
label1.pack()
label2.pack()
label3.pack()

root.mainloop()
