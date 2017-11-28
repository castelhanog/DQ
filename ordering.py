from tkinter import *
import shelve
from custom import *

class Pedidos(object):
    def __init__(self, c):
        self.c = c
        self.c['bg'] = color
        self.dbo1 = shelve.open('order1')
        self.dbo2 = shelve.open('order2')
        self.dbo3 = shelve.open('order3')
        self.dbo4 = shelve.open('order4')

        self.telaprincipal()

    def telaprincipal(self):
        self.l1 = Label(self.c, text='Módulo de Pedidos', bg=color)
        self.l1.grid(row=1, column=1, columnspan=2, padx=5)

        self.l2 = Label(self.c, text='Escolha o produto, informe o cliente e quantidade', bg=color)
        self.l2.grid(row=2, column=1, columnspan=2, padx=5)

        self.p = IntVar()

        self.rb1 = Radiobutton(self.c, text='Pãozinho doce simples', variable=self.p, value=0, bg=color)
        self.rb1.grid(row=3, column=1, padx=3)

        self.rb2 = Radiobutton(self.c, text='Pãozinho doce recheado', variable=self.p, value=1, bg=color)
        self.rb2.grid(row=4, column=1, padx=3)

        self.rb3 = Radiobutton(self.c, text='Pãozinho salgado recheado', variable=self.p, value=2, bg=color)
        self.rb3.grid(row=3, column=2, padx=3)

        self.rb4 = Radiobutton(self.c, text='Brownie', variable=self.p, value=3, bg=color)
        self.rb4.grid(row=4, column=2, padx=3)

        self.l3 = Label(self.c, text='Cliente', bg=color)
        self.l3.grid(row=5, column=1, columnspan=2, padx=5)

        self.e1 = Entry(self.c)
        self.e1.grid(row=6, column=1, columnspan=2, padx=5)

        self.l4 = Label(self.c, text='Quantidade', bg=color)
        self.l4.grid(row=7, column=1, columnspan=2, padx=5)

        self.e2 = Entry(self.c)
        self.e2.grid(row=8, column=1, columnspan=2, padx=5)

        self.l5 = Label(self.c, text="", bg=color)
        self.l5.grid(row=9, column=1, columnspan=2, padx=4)

        self.b1 = Button(self.c, text='Grava')
        self.b1.bind('<Button-1>', self.gravapedido)
        self.b1.bind('<Return>', self.gravapedido)
        self.b1.grid(row=10, column=1, padx=3)

        self.b2 = Button(self.c, text='Gera Pedido')
        self.b2.bind('<Button - 1>', self.gerapedido)
        self.b2.bind('<Return>', self.gerapedido)
        self.b2.grid(row=10, column=2, padx=3)

    def gravapedido(self, event):
        c = self.e1.get()
        q = self.e2.get()

        if self.p.get() == 0:
            if c not in self.dbo1:
                self.dbo1[c] = q
                self.l5['text'] = 'Pedido de Pãozinho simples para %s. Quantidade: %s' % (c,q)
            elif c in self.dbo1:
                self.dbo1[c] += q
                self.l5['text'] = 'Pedido de Pãozinho simples para %s. Quantidade: %s' % (c, q)
        elif self.p.get() == 1:
            if c not in self.dbo2:
                self.dbo2[c] = q
                self.l5['text'] = 'Pedido de Pãozinho doce recheado para %s. Quantidade: %s' % (c, q)
            elif c in self.dbo2:
                self.dbo2[c] += q
                self.l5['text'] = 'Pedido de Pãozinho doce recheado para %s. Quantidade: %s' % (c, q)
        elif self.p.get() == 2:
            if c not in self.dbo3:
                self.dbo3[c] = q
                self.l5['text'] = 'Pedido de Pãozinho salgado recheado para %s. Quantidade: %s' % (c, q)
            elif c in self.dbo3:
                self.dbo3[c] += q
                self.l5['text'] = 'Pedido de Pãozinho salgado recheado para %s. Quantidade: %s' % (c, q)
        elif self.p.get() == 3:
            if c not in self.dbo4:
                self.dbo4[c] = q
                self.l5['text'] = 'Pedido de Brownie para %s. Quantidade: %s' % (c, q)
            elif c in self.dbo4:
                self.dbo4[c] = q
                self.l5['text'] = 'Pedido de Brownie para %s. Quantidade: %s' % (c, q)

    def gerapedido(self, event):
        for i in self.dbo1:
            print('Pãozinho doce')
            print(i + ':' + self.dbo1[i])

z = Tk()
z.title('V 0.2')
z.resizable(False, False)
Pedidos(z)
z.mainloop()
