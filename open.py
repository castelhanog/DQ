import shelve
from tkinter import *
from custom import *
from connection import Conecta
from sell import principal
from ordering import Pedidos


class Login(object):
    def __init__(self,b):
        self.b = b
        self.b['bg'] = color
        self.dbl = shelve.open('access')
        self.dbl['OPENER'] = 'SUPERACCESS'

        self.telaprincipal()

    def telaprincipal(self):

        self.l1 = Label(self.b, text = 'Bem - vindo!', bg = color, fg = 'white', font = font1)
        self.l1.grid(row = 1, column = 1, columnspan = 2, padx = 5)

        self.l2 = Label(self.b, text = 'Faça login e escolha um modo para entrar', bg = color, fg = 'white', font = font3)
        self.l2.grid(row = 2, column = 1, columnspan = 2, padx = 5)

        self.l3 = Label(self.b, text = 'Usuário', bg = color, fg = 'white', font = font3)
        self.l3.grid(row = 3, column = 1, columnspan = 2, padx =3)

        self.e1 = Entry(self.b)
        self.e1.grid(row = 4, column = 1, columnspan = 2)

        self.l4 = Label(self.b, text = 'Senha', bg = color, fg = 'white', font = font3)
        self.l4.grid(row = 5, column = 1, columnspan = 2, padx = 3)

        self.e2 = Entry(self.b, show = '*')
        self.e2.grid(row = 6, column = 1, columnspan = 2)
        '''
        Usar intvar() para atribuir a variable no radio button para que ele troque, bem como atribuir
        value crescente para cada radio button criado.
        '''
        self.r = IntVar()
        self.rb1 = Radiobutton(self.b, text = 'Módulo Venda', variable = self.r, value = 0, bg = color)
        self.rb1.grid(row = 7, column = 1, columnspan = 2)

        self.rb2 = Radiobutton(self.b, text = 'Módulo Pedidos', variable = self.r, value = 1, bg = color)
        self.rb2.grid(row = 8, column = 1, columnspan = 2)

        self.l5 = Label(self.b, text = "", bg = color, fg = 'white', font = font2)
        self.l5.grid(row = 9, column = 1, columnspan = 2)

        self.b1 = Button(self.b, text = 'Entrar')
        self.b1.bind('<Button-1>', self.entrar)
        self.b1.bind('<Return>', self.entrar)
        self.b1.grid(row = 10, column = 1)

        self.b2 = Button(self.b, text = 'Novo usuário')
        self.b2.bind('<Button-1>', self.novo)
        self.b2.bind('<Return>', self.novo)
        self.b2.grid(row = 10, column = 2)

        self.new = False

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
            elif self.dbl[c] == s and (self.r.get() == 0):
                self.muda()
            elif self.dbl[c] == s and (self.r.get() == 1):
                self.muda1()

    def muda(self):
        self.destroi()
        principal(self.b)

    def muda1(self):
        self.destroi()
        Pedidos(self.b)

    def destroi(self):
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        self.l5.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.rb1.destroy()
        self.rb2.destroy()

    def novo(self, event):
        if not self.new:
            self.l2['text'] = 'Digite um novo usuário e nova senha'
            self.b2['text'] = 'Criar'
            self.new = True
        else:
            self.cria()

    def cria(self):
        c = self.e1.get()
        s = self.e2.get()

        c = c.upper()
        s = s.upper()

        if c or s !="":

            self.c = Conecta()
            self.dados = self.c.ledadosUsuarios(c,s)

            if c == self.dados[2]:
                self.l5['text'] = 'Usuário já cadastrado!'
            else:
                self.c.insereDadosUsuarios(c,s)
                self.l5['text'] = 'Usuário cadastrado com sucesso'
                self.new = False
        else:
               self.l5['text'] = 'Preencha os campos de usuário e senha'

l = Tk()

l.title('Login')

l.resizable(False, False)

Login(l)

l.mainloop()
