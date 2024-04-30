from tkinter import *

root = Tk()
root.geometry('300x200')

s1 = Spinbox(root, from_=0, to=10)
s1.pack()
s2 = Spinbox(root, values=(10,20,30, 35,40,55), wrap=True)
s2.pack()
s3 = Spinbox(root, values=('Caio', 'Tício', 'Mévio'))
s3.pack()

def executar():
    print(s2.get())

cmd = Button(root, text='Run', command=executar)
cmd.pack()

root.mainloop()
