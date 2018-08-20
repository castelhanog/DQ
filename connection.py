import sqlite3

class Conecta(object):
    def __init__(self):
        self.conect()

    def conect(self):
        self.con = sqlite3.connect('db.db')

    def fechaConexao(self):
        self.con.close()

    def defineCursor(self):
        self.cursor = self.con.cursor()

    def insereDadosUsuarios(self, login, senha):
        self.defineCursor()
        self.cursor.execute("""
        INSERT INTO usuario(login, senha)
        values(?,?)
        """,(login, senha))

        self.comita()

    def ledadosUsuarios(self, login, senha):
        self.defineCursor()
        self.cursor.execute("""
        SELECT * FROM usuario
        """)

        for i in self.cursor.fetchall():
                return i


    def comita(self):
        self.con.commit()
        self.fechaConexao()


if __name__ == '__main__':
    c = Conecta()