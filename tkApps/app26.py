from tkinter import *

class MinhaFrame(Frame): # herança Frame
    def __init__(self, parent): # contrutor
        super().__init__() # chama construtor de frame
        
        self.label1_text = StringVar()
        self.text1_text = StringVar()
        
        self.label1 = Label(self, textvariable = self.label1_text).pack()
        text1 = Entry(self, textvariable = self.text1_text).pack()
        cmd1 = Button(self, text = 'Clique', command = self.Executar).pack()
        
    def Executar(self):
        self.label1_text.set('Olá Mundo! ' + self.text1_text.get() + '.')

root = Tk()

frame1 = MinhaFrame(root).pack()
frame2 = MinhaFrame(root).pack()

root.mainloop()