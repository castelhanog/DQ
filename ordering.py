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

        self.l5 = Label(self.c, text="", bg=color, fg='white', font=font2)
        self.l5.grid(row=11, column=1, columnspan=2)

        self.l6 = Label(self.c, text="", bg=color, fg='white', font=font2)
        self.l6.grid(row=11, column=1, columnspan=2)

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

        self.p = Conecta()
        # lembrar de colocar o comando sql ao chamar o método abaixo
        self.cliente = self.p.ledados('SELECT * FROM pedidos WHERE nome_cliente=?',(c,))

        if self.cliente != []:

            '''
            IMPORTANTE!!!! Depois de horas tentando realizar o update quando já tivesse cliente e produtos, e gravar um produto novo,
            quando já tivesse o cliente, depois de muita batalha (estava indo pro banco novamente mesmo já existente), isto por conta
            do for loop, em um loop ele achava, fazia o upload e continuava, no outro, como estaria diferente ele gravava outro registro duplicadp
            no banco. A solução, embora penosa, é simples. ao invés de tentar fazer tudo com o retorno de uma query (usando o self.cliente acima)
            eu executo uma para cada option. Assim, ele não vai percorrer todos os resuldados. Portanto faz o update se achar cliente e produto juntos
            ou grava um registro novo se achar cliente e não achar produto. 
            Depois de muito tempo perdido, fica a lição de que nem sempre tentar simplificar o máximo deu certo.
            O ponto chave não está no self.cliente e sim no self.verifica1 dentro dos options
            '''
            if self.var.get() != "Escolha um produto":
                self.verifica1 = self.p.ledados('SELECT * FROM pedidos WHERE nome_cliente=? AND produto=?',(c, self.var.get(), ))
                if self.verifica1 != []:
                    self.q1 = int(self.p.transformaResultados(self.p.ledados('''
                    SELECT quantidade 
                    FROM pedidos 
                    WHERE nome_cliente = ? AND produto = ?
                    ''', (c, self.var.get()))))
                    self.p.executaUpdatePedidos(c, self.var.get(), (self.q1 + int(self.e2.get())), t)

                else:
                    self.valida = int(self.e2.get())
                    if self.valida > 0:
                        self.p.insereDadosPedidos(c, self.var.get(), self.e2.get(), t)
                    else:
                        pass

            if self.var2.get() != "Escolha um produto":
                self.verifica2 = self.p.ledados('SELECT * FROM pedidos WHERE nome_cliente=? AND produto=?',(c, self.var2.get(), ))
                if self.verifica2 != []:
                    self.q2 = int(self.p.transformaResultados(self.p.ledados('''
                    SELECT quantidade 
                    FROM pedidos 
                    WHERE nome_cliente = ? AND produto = ?
                    ''', (c, self.var2.get()))))
                    self.p.executaUpdatePedidos(c, self.var2.get(), (self.q2 + int(self.e3.get())), t)

                else:
                    self.valida2 = int(self.e3.get())
                    if self.valida2 > 0:
                        self.p.insereDadosPedidos(c, self.var2.get(), self.e3.get(), t)
                    else:
                        pass

            if self.var3.get() != "Escolha um produto":
                self.verifica3 = self.p.ledados('SELECT * FROM pedidos WHERE nome_cliente=? AND produto=?',(c, self.var3.get(), ))
                if self.verifica3 != []:
                    self.q3 = int(self.p.transformaResultados(self.p.ledados('''
                    SELECT quantidade 
                    FROM pedidos 
                    WHERE nome_cliente = ? AND produto = ?
                    ''', (c, self.var3.get()))))
                    self.p.executaUpdatePedidos(c, self.var3.get(), (self.q3 + int(self.e4.get())), t)

                else:
                    self.valida3 = int(self.e4.get())
                    if self.valida3 > 0:
                        self.p.insereDadosPedidos(c, self.var3.get(), self.e4.get(), t)
                    else:
                        pass

            if self.var4.get() != "Escolha um produto":
                self.verifica4 = self.p.ledados('SELECT * FROM pedidos WHERE nome_cliente=? AND produto=?',(c, self.var4.get(), ))
                if self.verifica4 != []:
                    self.q4 = int(self.p.transformaResultados(self.p.ledados('''
                    SELECT quantidade 
                    FROM pedidos 
                    WHERE nome_cliente = ? AND produto = ?
                    ''', (c, self.var4.get()))))
                    self.p.executaUpdatePedidos(c, self.var4.get(), (self.q4 + int(self.e5.get())), t)

                else:
                    self.valida4 = int(self.e5.get())
                    if self.valida4 > 0:
                        self.p.insereDadosPedidos(c, self.var4.get(), self.e5.get(), t)
                    else:
                        pass

        else:
            if self.var.get() != "Escolha um produto":
                self.p.insereDadosPedidos(c, self.var.get(), self.e2.get(), t)
            else:
                pass
            if self.var2.get() != "Escolha um produto":
                self.p.insereDadosPedidos(c, self.var2.get(), self.e3.get(), t)
            else:
                pass
            if self.var3.get() != "Escolha um produto":
                self.p.insereDadosPedidos(c, self.var3.get(), self.e4.get(), t)
            else:
                pass
            if self.var4.get() != "Escolha um produto":
                self.p.insereDadosPedidos(c, self.var4.get(), self.e5.get(), t)
            else:
                pass
            self.gerado()

        self.con.fechaConexao()

    def gerado(self):
        self.gerado = Tk()
        self.gerado.title('Clientes e Saldos')

        self.t = Text(self.gerado)
        self.t.pack()


            # atualizado 06/10/2018 . update e gravar pedido, terminados.


    def gerapedido(self, event):
        arquivo = open('Pedido.txt', 'w')

        self.g = Conecta()

        self.consultapedido = self.g.ledados('SELECT * FROM pedidos')

        if self.consultapedido != []:

            for i in self.consultapedido:

                arquivo.write('Cliente: %s Produto: %s Quantidade: %s\n' % (i[1], i[2], str(i[3])))
        
        self.l5['text'] = 'Pedido gerado com sucesso!'
        self.l5['font'] = font2
        arquivo.close()


if __name__ == '__main__':
    z = Tk()
    z.title('V 0.2')
    z.resizable(False, False)
    Pedidos(z)
    z.mainloop()
