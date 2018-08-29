from tkinter import *
from custom import *
from connection import Conecta
import time

class Pedidos(object):
    def __init__(self, c):
        self.c = c
        self.c['bg'] = color

        self.telaprincipal()

    def telaprincipal(self):
        self.l1 = Label(self.c, text='Módulo de Pedidos', bg = color, fg = 'white', font = font1)
        self.l1.grid(row=1, column=1, columnspan=3, padx=5)

        self.l2 = Label(self.c, text='Escolha o produto, informe o cliente e quantidade', bg = color, fg = 'white', font = font2)
        self.l2.grid(row=2, column=1, columnspan=3, padx=5)

        self.l3 = Label(self.c, text='Cliente', bg=color, fg = "white", font=font3)
        self.l3.grid(row=3, column=1, columnspan=3, padx=5)

        self.e1 = Entry(self.c)
        self.e1.grid(row=4, column=1, columnspan=3, padx=5)

        self.l4 = Label(self.c, text="", bg=color)
        self.l4.grid(row=9, column=1, columnspan=2, padx=4)

        #primeira opção
        self.con = Conecta()
        self.produtos = self.con.ledados("SELECT produto_nome FROM produtos")

        lista = [] #lista com os resultados da query para exibição no option

        for i in self.produtos:
            lista.append(str(i[0])) #adicionando resultados fora da tupla para a lista

        self.var = StringVar(self.c) #verificar necessidade na documentação de optionmenu tkinter.
        self.var.set("Escolha um produto")  # valor exibido no botão

        self.option1 = OptionMenu(self.c, self.var, *lista) # colocar '*' antes da variavel lista para
        self.option1.grid(row=6, column=1, columnspan=2, padx=5) #que sejam exibidas todas as opçães, uma em cada linha

        self.l5 = Label(self.c, text='Quantidade', bg=color, fg = "white", font=font3)
        self.l5.grid(row=5, column=3, columnspan=3, padx=5)

        self.e2 = Entry(self.c)
        self.e2.grid(row=6, column=3, columnspan=3, padx=5)

        self.l6 = Label(self.c, text="", bg=color)
        self.l6.grid(row=9, column=1, columnspan=2, padx=4)

        # segunda opção
        self.con = Conecta()
        self.produtos = self.con.ledados("SELECT produto_nome FROM produtos")

        lista = []  # lista com os resultados da query para exibição no option

        for i in self.produtos:
            lista.append(str(i[0]))  # adicionando resultados fora da tupla para a lista

        self.var2 = StringVar(self.c)
        self.var2.set("Escolha um produto")  # valor exibido no botão

        self.option2 = OptionMenu(self.c, self.var2, *lista)  # colocar '*' antes da variavel lista para
        self.option2.grid(row=8, column=1, columnspan=2, padx=5)  # que sejam exibidas todas as opçães, uma em cada linha

        self.l5 = Label(self.c, text='Quantidade', bg=color, fg="white", font=font3)
        self.l5.grid(row=7, column=3, columnspan=3, padx=5)

        self.e3 = Entry(self.c)
        self.e3.grid(row=8, column=3, columnspan=3, padx=5)

        self.l6 = Label(self.c, text="", bg=color)
        self.l6.grid(row=9, column=1, columnspan=2, padx=4)

        # terceira opção
        self.con = Conecta()
        self.produtos = self.con.ledados("SELECT produto_nome FROM produtos")

        lista = []  # lista com os resultados da query para exibição no option

        for i in self.produtos:
            lista.append(str(i[0]))  # adicionando resultados fora da tupla para a lista

        self.var3 = StringVar(self.c)
        self.var3.set("Escolha um produto")  # valor exibido no botão

        self.option3 = OptionMenu(self.c, self.var3, *lista)  # colocar '*' antes da variavel lista para
        self.option3.grid(row=10, column=1, columnspan=2, padx=5)  # que sejam exibidas todas as opçães, uma em cada linha

        self.l5 = Label(self.c, text='Quantidade', bg=color, fg="white", font=font3)
        self.l5.grid(row=9, column=3, columnspan=3, padx=5)

        self.e4 = Entry(self.c)
        self.e4.grid(row=10, column=3, columnspan=3, padx=5)

        self.l6 = Label(self.c, text="", bg=color)
        self.l6.grid(row=11, column=1, columnspan=2, padx=4)

        # quarta opção
        self.con = Conecta()
        self.produtos = self.con.ledados("SELECT produto_nome FROM produtos")

        lista = []  # lista com os resultados da query para exibição no option

        for i in self.produtos:
            lista.append(str(i[0]))  # adicionando resultados fora da tupla para a lista

        self.var4 = StringVar(self.c)
        self.var4.set("Escolha um produto")  # valor exibido no botão

        self.option4 = OptionMenu(self.c, self.var4, *lista)  # colocar '*' antes da variavel lista para
        self.option4.grid(row=12, column=1, columnspan=2, padx=5)  # que sejam exibidas todas as opçães, uma em cada linha

        self.l5 = Label(self.c, text='Quantidade', bg=color, fg="white", font=font3)
        self.l5.grid(row=11, column=3, columnspan=3, padx=5)

        self.e5 = Entry(self.c)
        self.e5.grid(row=12, column=3, columnspan=3, padx=5)

        self.l6 = Label(self.c, text="", bg=color)
        self.l6.grid(row=13, column=1, columnspan=2, padx=4)

        self.b1 = Button(self.c, text='Grava')
        self.b1.bind('<Button-1>', self.gravapedido)
        self.b1.bind('<Return>', self.gravapedido)
        self.b1.grid(row=14, column=1, padx=3)

        self.b2 = Button(self.c, text='Gera Pedido')
        self.b2.bind('<Button - 1>', self.gerapedido)
        self.b2.bind('<Return>', self.gerapedido)
        self.b2.grid(row=14, column=3, padx=3)

    def gravapedido(self, event):
        c = self.e1.get()
        t = time.strftime("%x, %X")

        c = c.upper()

        print(self.var.get(), self.var2.get(), self.var3.get(), self.var4.get())

        self.p = Conecta()
        # lembrar de colocar o comando sql ao chamar o método abaixo
        self.cliente = self.p.ledados('SELECT * FROM usuario')
        for i in self.cliente:
            # Transformar resultado em lista para facilitar o acesso aos indíces de i
            i = list(i)
            if c not in i:
                if self.var.get() != "Escolha um produto":
                    self.p.insereDadosPedidos(c, self.var.get(),self.e2.get(), t)
                if self.var2.get() != "Escolha um produto":
                    self.p.insereDadosPedidos(c, self.var2.get(),self.e3.get(), t)
                if self.var3.get() != "Escolha um produto":
                    self.p.insereDadosPedidos(c, self.var3.get(),self.e4.get(), t)
                if self.var4.get() != "Escolha um produto":
                    self.p.insereDadosPedidos(c, self.var4.get(),self.e5.get(), t)
                self.p.fechaConexao()



    def gerapedido(self, event):
        arquivo = open('Pedido.txt', 'w')

        if len(self.dbo1) > 0:
            arquivo.write('Pãozinho simples\n\n')
            for i in self.dbo1:
                arquivo.write('%s: %s\n' % (i, str(self.dbo1[i])))

        if len(self.dbo2) > 0:
            arquivo.write('\nPãozinho doce recheado\n\n')
            for i in self.dbo2:
                arquivo.write('%s: %s\n' % (i, str(self.dbo2[i])))

        if len(self.dbo3) > 0:
            arquivo.write('\nPãozinho salgado recheado\n\n')
            for i in self.dbo3:
                arquivo.write('%s: %s\n' % (i, str(self.dbo3[i])))

        if len(self.dbo4) > 0:
            arquivo.write('\nBrownie\n\n')
            for i in self.dbo4:
                arquivo.write('%s: %s\n' % (i, str(self.dbo4[i])))
        self.l5['text'] = 'Pedido gerado com sucesso!'
        self.l5['font'] = font2
        arquivo.close()
        self.dbo1.clear()
        self.dbo2.clear()
        self.dbo3.clear()
        self.dbo4.clear()

if __name__ == '__main__':
    z = Tk()
    z.title('V 0.2')
    z.resizable(False, False)
    Pedidos(z)
    z.mainloop()
