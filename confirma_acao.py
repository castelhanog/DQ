from tkinter import *
from custom import *

class Confirma(object):
    def __init__(self,d):
        self.d = d
        self.b['bg'] = color

        self.telaprincipal()

    def telaprincipal(self):

        self.l1 = Label(self.b, text = 'Operação realizada com sucesso', bg = color, fg = 'white', font = font1)
        self.l1.grid(row = 1, column = 1, columnspan = 2, padx = 5)

        self.b1 = Button(self.b, text='Fechar')
        self.b1.bind('<Button-1>', self.fecha)
        self.b1.bind('<Return>', self.fecha)
        self.b1.grid(row=12, column=1)

    def destroi(self):
        self.l1.destroy()
        self.b1.destroy()


l = Tk()

l.title('Operação Concluída')

l.resizable(False, False)

Confirma(l)

l.mainloop()