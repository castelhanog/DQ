from tkinter import *
import shelve

class Login(object):
    def __init__(self,b):
        self.b = b
        self.dbl = shelve.open('access')
        self.dbl['opener'] = 'superaccess'

        self.l1 = Label(self.b, text = 'Bem - vindo!')
        self.l1.grid(row = 1, column = 1, padx = 5)

        self.l2 = Label(self.b, text = 'Faça login e escolha um modo para entrar')
        self.l2.grid(row = 2, column = 1, padx = 5)

        self.l3 = Label(self.b, text = 'Usuário')
        self.l3.grid(row = 3, column = 1, padx =3)

        self.e1 = Entry(self.b)
        self.e1.grid(row = 4, column = 1)

        self.l4 = Label(self.b, text = 'Senha')
        self.l4.grid(row = 5, column = 1, padx = 3)

        self.e2 = Entry(self.b)
        self.e2.grid(row = 6, column = 1)

        self.l5 = Label(self.b, text = "")
        self.l5.grid(row = 7, column = 1)

        self.b1 = Button(self.b, text = 'Entrar')
        self.b1.grid(row = 8, column = 1)

l = Tk()

Login(l)

l.mainloop()