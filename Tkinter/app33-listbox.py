from tkinter import *

root = Tk()

list = Listbox(root)
list.pack()

list.insert(END,"Firs list item")
list.insert(END,"Second list item")

names = ['João', 'Ana', 'Carlos']
for name in names:
    list.insert(END, name)

#list.delete(1, 1)

def executar():
    print(list.get(ACTIVE))

cmd = Button(root, text='Click', command=executar).pack()

root.mainloop()
