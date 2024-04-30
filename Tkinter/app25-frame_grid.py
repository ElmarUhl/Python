from tkinter import *

root = Tk()
root.title("App")

frame_login = Frame(root)

labelUser = Label(frame_login, text="User:")
labelPassword = Label(frame_login, text="Password:")
textUser = Entry(frame_login)
textPassword = Entry(frame_login)
cmd = Button(frame_login,text="Enter")

labelUser.grid(row=0,column=0)
labelPassword.grid(row=1,column=0)
textUser.grid(row=0,column=1)
textPassword.grid(row=1,column=1)
cmd.grid(row=2,column=1)

frame_login.grid()

root.mainloop()
