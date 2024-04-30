from tkinter import *

class myFrame(Frame): # inherit
    def __init__(self, parent): # contructor
        super().__init__() # calls construtor de frame
        
        self.l1_text = StringVar()
        self.t1_text = StringVar()
        
        self.l1 = Label(self, textvariable = self.l1_text).pack()
        t1 = Entry(self, textvariable = self.t1_text).pack()
        cmd1 = Button(self, text = 'Click', command = self.Executar).pack()
        
    def Executar(self):
        self.l1_text.set('Hello world! ' + self.t1_text.get() + '.')

root = Tk()

f1 = myFrame(root).pack()
f2 = myFrame(root).pack()

root.mainloop()