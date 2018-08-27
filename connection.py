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

    def executaConsulta(self, sql, parms = None):
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


    def comita(self):
        self.con.commit()
        self.fechaConexao()


if __name__ == '__main__':
    c = Conecta()