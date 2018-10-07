import sqlite3

class Conecta(object):
    def __init__(self):
        self.conect()

    def conect(self):
        self.con = sqlite3.connect('db.db', timeout=1)

    def fechaConexao(self):
        self.con.close()

    def defineCursor(self):
        self.cursor = self.con.cursor()

    def insereDadosUsuarios(self, nome, login, senha, data_criacao):
        self.defineCursor()
        self.cursor.execute("""
        INSERT INTO usuario(nome, login, senha, data_criacao)
        values(?,?,?,?)
        """,(nome, login, senha, data_criacao))

        self.comita()

    def ledados(self, sql, parms = None):
        if parms == None:
            self.defineCursor()
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            self.defineCursor()
            self.cursor.execute(sql, parms)
            return self.cursor.fetchall()

    def insereDadosVendas(self, cliente, saldo, data_modificacao):
        self.defineCursor()
        self.cursor.execute("""
        INSERT INTO cliente_saldo(cliente, saldo, data_modificacao)
        values(?,?,?)
        """,(cliente, saldo, data_modificacao))

        self.comita()

    def insereDadosPedidos(self, nome_cliente, produto, quantidade, data_modificacao):
        self.defineCursor()
        self.cursor.execute("""
        INSERT INTO pedidos(nome_cliente, produto, quantidade, data_modificacao)
        values(?,?,?,?)
        """,(nome_cliente, produto, quantidade, data_modificacao))

        self.comita()

    def executaUpdatePedidos(self, nome_cliente, produto, quantidade, data_modificacao):
        self.defineCursor()
        self.cursor.execute("""
        UPDATE pedidos
        SET quantidade=?, 
        data_modificacao=?
        WHERE nome_cliente=? AND produto=?
        """,(quantidade, data_modificacao, nome_cliente, produto))
        self.comita()

    def executaConsulta(self, sql, parms = None):
        if parms == None:
            self.defineCursor()
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            self.defineCursor()
            self.cursor.execute(sql, parms)
            return self.cursor.fetchall()

    def executaConsulta(self, ):
        if parms == None:
            self.defineCursor()
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        else:
            self.defineCursor()
            self.cursor.execute(sql, parms)
            return self.cursor.fetchall()

    def executaUpdate(self, sql, parms = None):
        if parms == None:
            self.defineCursor()
            self.cursor.execute(sql)
            self.comita()
        else:
            self.defineCursor()
            self.cursor.execute(sql, parms)
            self.comita()

    def transformaResultados(self, value):
        self.trata = value
        for i in self.trata:
            for b in i:
                return b


    def comita(self):
        self.con.commit()



if __name__ == '__main__':
    c = Conecta()