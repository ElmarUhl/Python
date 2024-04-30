from tkinter import *

def executar():
    l1["text"] = t1.get()
    l2["text"] = t2.get()
    l3["text"] = t3.get()
    
root = Tk()
root.title("App")

# Attention! The focus obeys this order
t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

l1 = Label(root)
l2 = Label(root)
l3 = Label(root)

b = Button(root, text="Run", command=executar)

t1.grid()
t2.grid()
t3.grid()

l1.grid()
l2.grid()
l3.grid()

b.grid()

t1.focus()

root.mainloop()
