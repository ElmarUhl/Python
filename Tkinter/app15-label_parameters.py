from tkinter import *

root = Tk()
root.title("Title")
root.geometry("500x300")

l1 = Label(
    root,
    text= "Test phrase",
    font="Arial 20",
    bd=1,
    relief="solid"
)
l1.pack()

l2 = Label(root)
l2["text"]= "Test phrase"
l2['font'] = "Arial 12"
l2['bd'] = 1
l2['relief'] = "solid"
l2.pack()

l2['text'] = "New text"

print(l2.keys())

for item in l2.keys():
    print(item, " : ", l2[item])

root.mainloop()
