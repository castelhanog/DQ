from tkinter import *
import shelve
from custom import *


class principal(object):
    def __init__(self, a):
        self.a = a
        self.a['bg'] = color
        self.dbs = shelve.open('selldb')

        self.l1 = Label(self.a, text = 'Módulo de vendas', bg = color, fg = 'white', font = font1)
        self.l1.grid(row = 1, column = 2, pady = 3)

        self.l2 = Label(self.a, text = 'Cliente', bg = color, font = font3)
        self.l2.grid(row = 2, column = 2, pady = 3)

        self.e1 = Entry(self.a)
        self.e1.grid(row = 3, column = 2, pady = 3)

        self.l3 = Label(self.a, text = "Valor", bg = color, font = font3)
        self.l3.grid(row = 4, column = 2, pady = 3)

        self.e2 = Entry(self.a)
        self.e2.grid(row = 5, column = 2, pady = 3)

        self.l5 = Label(self.a, text = "", bg = color, pady = 3, font = font2)
        self.l5['bg'] = color
        self.l5.grid(row = 6, column = 2)

        self.b1 = Button(self.a, text ='Registra venda')
        self.b1.bind('<Button-1>', self.venda)
        self.b1.bind('<Return>', self.venda)
        self.b1.grid(row = 7, column = 1)

        self.b2 = Button(self.a, text = 'Abater valor')
        self.b2.bind('<Button-1>', self.abate)
        self.b2.bind('<Return>', self.abate)
        self.b2.grid(row = 7, column = 2)

        self.b3 = Button(self.a, text = 'Ver saldo')
        self.b3.bind('<Button-1>', self.saldo)
        self.b3.bind('<Return>', self.saldo)
        self.b3.grid(row = 7, column = 3)

    def venda(self, event):
        c = self.e1.get()
        v = self.e2.get()

        c = c.upper()
        v = float(v.replace(',','.'))

        if c not in self.dbs:
            self.dbs[c] = float(v)
            self.l5['text'] = 'Venda no valor de R$ %.2f registrada para %s' % (v, c)
        elif c in self.dbs:
            self.dbs[c] += float(v)
            self.l5['text'] = 'Venda no valor de R$ %.2f registrada para %s' % (v, c)

    def abate(self, event):
        c = self.e1.get()
        v = self.e2.get()

        c = c.upper()
        v = float(v.replace(',', '.'))

        if c not in self.dbs:
            self.l5['text'] = 'Usuário não encontrado'
        elif c in self.dbs:
            self.dbs[c] -= float(v)
            self.l5['text'] = 'Valor de RS %.2f abatido do cliente %s' % (v,c)

    def saldo(self, event):
        c = self.e1.get()
        c = c.upper()

        if c not in self.dbs:
            self.l5['text'] = "Usuário não encontrado no cadastro"
        elif c in self.dbs:
            self.l5['text'] = "%s tem um saldo de %.2f" % (c, self.dbs[c])


i = Tk()

i.title('V 0.1')

principal(i)

i.mainloop()