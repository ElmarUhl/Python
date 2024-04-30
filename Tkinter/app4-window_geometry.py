from tkinter import *

menu_initial = Tk()

menu_initial.title("First App") # Window title

menu_initial.geometry("500x250+200+200") # Window size and position
menu_initial.resizable(True,True)

menu_initial.minsize(100,100)
menu_initial.maxsize(600,480)

menu_initial.mainloop()
