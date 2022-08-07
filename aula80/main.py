import sqlite3
import os


pasta_atual = os.path.dirname(__file__)


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenta SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agena WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)
        
        for linha in self.cursor.fetchall():
            identificador, nome, telefone = linha
            print(identificador, nome, telefone)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        
        for linha in self.cursor.fetchall():
            identificador, nome, telefone = linha
            print(identificador, nome, telefone)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB(f'{pasta_atual}/agenda.db')
    #agenda.inserir('Julio C.', '41900000000')
    #agenda.inserir('Luana P.', '41911111111')
    #agenda.inserir('Giovanna C.', '41922222222')
    #agenda.inserir('Guilherme', '41933333333')
    #agenda.inserir('Caua', '41944444444')
    #agenda.inserir('João', '41955555555')
    #agenda.inserir('Fabrício', '41966666666')
    #agenda.buscar('a')
    agenda.fechar()

