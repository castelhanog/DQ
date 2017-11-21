from tkinter import *
import shelve

class Login(object):
    def __init__(self,b):
        self.b = b
        self.dbl = shelve.open('access')
        self.dbl['OPENER'] = 'SUPERACCESS'

        self.l1 = Label(self.b, text = 'Bem - vindo!')
        self.l1.grid(row = 1, column = 1, columnspan = 2, padx = 5)

        self.l2 = Label(self.b, text = 'Faça login e escolha um modo para entrar')
        self.l2.grid(row = 2, column = 1, columnspan = 2, padx = 5)

        self.l3 = Label(self.b, text = 'Usuário')
        self.l3.grid(row = 3, column = 1, columnspan = 2, padx =3)

        self.e1 = Entry(self.b)
        self.e1.grid(row = 4, column = 1, columnspan = 2)

        self.l4 = Label(self.b, text = 'Senha')
        self.l4.grid(row = 5, column = 1, columnspan = 2, padx = 3)

        self.e2 = Entry(self.b, show = '*')
        self.e2.grid(row = 6, column = 1, columnspan = 2)

        self.rb1 = Radiobutton(self.b, text = 'Módulo Venda', value = 0)
        self.rb1.grid(row = 7, column = 1, columnspan = 2)

        self.rb1 = Radiobutton(self.b, text = 'Módulo Pedidos', value = 1)
        self.rb1.grid(row = 8, column = 1, columnspan = 2)

        self.l5 = Label(self.b, text = "")
        self.l5.grid(row = 9, column = 1, columnspan = 2)

        self.b1 = Button(self.b, text = 'Entrar')
        self.b1.bind('<Button-1>', self.entrar)
        self.b1.bind('<Return>', self.entrar)
        self.b1.grid(row = 10, column = 1)

        self.b2 = Button(self.b, text = 'Novo usuário')
        self.b2.bind('<Button-1>', self.novo)
        self.b2.bind('<Return>', self.novo)
        self.b2.grid(row = 10, column = 2)

    def entrar(self, event):
        c = self.e1.get()
        s = self.e2.get()

        c = c.upper()
        s = s.upper()

        if c not in self.dbl:
            self.l5['text'] = 'Usuário não encontrado!'

        elif c in self.dbl:
            if self.dbl[c] != s:
                self.l5['text'] = 'Senha incorreta!'
            elif self.dbl[c] == s:
                self.l5['text'] = 'Bem-vindo'

    def novo(self, event):
        return None

l = Tk()

Login(l)

l.mainloop()