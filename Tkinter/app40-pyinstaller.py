from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('Tela')

text = StringVar()
text.set('Any Text')

def changeText():
    text.set('New text')

l = Label(root, textvariable=text)
cmd = Button(root, text='Run', command=changeText)

l.pack()
cmd.pack()

root.mainloop()
