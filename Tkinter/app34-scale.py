from tkinter import *

root = Tk()
root.geometry('300x200')

# Obs. get() is not working with Scale().pack()
def showValue():
    print(s.get())

s = Scale(root, from_=0, to=100, orient='horizontal',resolution=0.5)
b = Button(root, text='Mostrar', command=showValue)

s.pack()
b.pack()

root.mainloop()
