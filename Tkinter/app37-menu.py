from tkinter import *

root = Tk()
root.geometry('300x200')

def file():
    print('File')

myMenu = Menu(root)
#myMenu.add_command(label='File', command=file)
#myMenu.add_command(label='File')
#myMenu.add_command(label='Edit')

fileMenu = Menu(myMenu, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exit)
myMenu.add_cascade(label='File', menu=fileMenu)

fileEdit = Menu(myMenu)
fileEdit.add_command(label='Cut')
fileEdit.add_command(label='Copy')
fileEdit.add_command(label='Paste')
myMenu.add_cascade(label='Edit', menu=fileEdit)

root.config(menu=myMenu)

root = mainloop()
