from tkinter import *

menu = Tk()
menu.title("Title")

width = 500
height = 300

widthScreen = menu.winfo_screenwidth()
heightScreen = menu.winfo_screenheight()

print(widthScreen,heightScreen)

posx = (widthScreen - width)/2
posy = (heightScreen - height)/2

menu.geometry("%dx%d+%d+%d" %(width, height, posx, posy))

menu.mainloop()
