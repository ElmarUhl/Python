from tkinter import *

root = Tk()

fName = Frame(root)
fAddress = Frame(root)

lName = Label(fName, text='Name:')
lNickName = Label(fName, text='Nick name:')
lStreet = Label(fAddress, text='Street:')
lCity = Label(fAddress, text='City:')

tName = Entry(fName)
tNickName = Entry(fName)
tStreet = Entry(fAddress)
tCity = Entry(fAddress)

cmd = Button(root, text='Save')

lName.grid(row=0, column=0)
lNickName.grid(row=1, column=0)
tName.grid(row=0, column=1)
tNickName.grid(row=1,column=1)

lStreet.grid(row=0, column=0)
lCity.grid(row=1, column=0)
tStreet.grid(row=0, column=1)
tCity.grid(row=1,column=1)

fName.grid()
fAddress.grid()
cmd.grid()

root.mainloop()
