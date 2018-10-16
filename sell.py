from tkinter import *
from custom import *
from connection import Conecta
import time


class principal(object):
    
    def __init__(self, a):
        self.a = a
        self.a['bg'] = color
        self.con = Conecta() #conectar já no __init__ para que após o login já esteja com conexão no banco.

        self.telaprincipal()

    def telaprincipal(self):

        self.l1 = Label(self.a, text = 'Módulo de vendas', bg = color, fg = 'white', font = font1)
        self.l1.grid(row = 2, column = 2, pady = 3)

        self.l2 = Label(self.a, text = 'Cliente', bg = color, font = font3)
        self.l2.grid(row = 3, column = 2, pady = 3)

        self.e1 = Entry(self.a)
        self.e1.grid(row = 4, column = 2, pady = 3)

        self.l3 = Label(self.a, text = "Valor", bg = color, font = font3)
        self.l3.grid(row = 5, column = 2, pady = 3)

        self.e2 = Entry(self.a)
        self.e2.grid(row = 6, column = 2, pady = 3)

        self.l5 = Label(self.a, text = "", bg = color, fg = "white", font = font2)
        self.l5['bg'] = color
        self.l5.grid(row = 7, column = 2, pady = 3)

        self.b1 = Button(self.a, text ='Registra venda')
        self.b1.bind('<Button-1>', self.venda)
        self.b1.bind('<Return>', self.venda)
        self.b1.grid(row = 8, column = 1)

        self.b2 = Button(self.a, text = 'Abater valor')
        self.b2.bind('<Button-1>', self.abate)
        self.b2.bind('<Return>', self.abate)
        self.b2.grid(row = 8, column = 2)

        self.b3 = Button(self.a, text = 'Clientes e Saldos')
        self.b3.bind('<Button-1>', self.saldo)
        self.b3.bind('<Return>', self.saldo)
        self.b3.grid(row = 8, column = 3)

    def venda(self, event):
        c = self.e1.get()
        v = self.e2.get()
        t = time.strftime("%x, %X")

        c = c.upper()
        v = float(v.replace(',', '.'))

        if type(v) == float:
            v = v
        else:
            v = None

        print(v)
        print(type(v))

        self.v = Conecta()
        self.dados = self.v.ledados("SELECT cliente FROM cliente_saldo")

        clientes = []

        for i in self.dados:
            for g in i:
                clientes.append(g)

        if c not in clientes:
            if v != None:
                self.v.insereDadosVendas(c,v,t)
                self.l5['text'] = 'Registrado o valor de R$ %.2f para cliente: %s' % (v, c)
            else:
                pass
                self.l5['text'] = 'Valor inserido inválido'

        else:
            if v != None:
                self.quantidade = float(self.v.transformaResultados(self.v.ledados('SELECT saldo FROM cliente_saldo WHERE cliente = ?',(c,))))
                self.v.executaUpdate("UPDATE cliente_saldo SET saldo = ? WHERE cliente = ?", (str(v + self.quantidade), c,))
                self.l5['text'] = 'Registrado o valor de R$ %.2f para cliente: %s' % (v, c)
            else:
                pass
                self.l5['text'] = 'Valor inserido inválido'

    def abate(self, event):
        c = self.e1.get()
        v = self.e2.get()
        t = time.strftime("%x, %X")

        c = c.upper()
        v = float(v.replace(',', '.'))

        self.v = Conecta()
        self.dados = self.v.ledados("SELECT cliente FROM cliente_saldo")

        if self.dados == []:
            self.v.insereDadosVendas(c, v, t)
            self.v.fechaConexao()
        else:
            for i in self.dados:
                if c in i:
                    saldo = self.v.ledados("SELECT saldo FROM cliente_saldo WHERE cliente = ?", (c,))

                    for h in saldo:
                        saldo1 = h[0]  # precisa fazer esse for pra tirar o resultado da tupla (verificar melhora no código)
                    saldo1 = float(saldo1)
                    saldo1 -= float(v)
                    self.v.executaUpdate("UPDATE cliente_saldo SET saldo = ? WHERE cliente = ?", (saldo1, c,))
                    self.v.fechaConexao()
                    time.sleep(0.3)
                    self.l5['text'] = 'Subtraído o valor de R$ %.2f para cliente: %s' % (v, c)
                    break
                elif c not in i:
                    continue  # break para para aqui se o if for verdadeiro, senão vai continuar (é errado)


    def saldo(self, event):
        self.saldo = Tk()
        self.saldo.title('Clientes e Saldos')

        self.t = Text(self.saldo)
        self.t.pack()

        self.s = Conecta()
        self.pesquisa_valores = self.s.ledados("SELECT cliente,saldo FROM cliente_saldo")

        for i in self.pesquisa_valores:
            consumer = i[0]
            value = i[1]
            self.t.insert(INSERT, '%s: R$ %s\n' % (consumer, str(value)))


if __name__ == '__main__':
    i = Tk()
    i.title('Venta - Versão 0.3')
    i.resizable(False, False)
    principal(i)
    i.mainloop()
