#aula  sobre SQLite3 + DB Browser for SQLite

import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()


    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,)) #ao final dos valores na tupla, deve ser inserido uma virgula
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',)) #o símbolo '%' significa qualquer coisa, no caso, para os lados
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Luiz', '123456')
    # agenda.inserir('Maria', '125456')
    # agenda.inserir('João', '323456')
    # agenda.inserir('Rosa', '129456')
    # agenda.inserir('Guilherme', '123886')
    # agenda.inserir('Luiza', '127756')
    # agenda.editar('Francisco', '124599', 6)
    # agenda.excluir(6)
    # agenda.inserir('Luiz Roberto', '993456')
    # agenda.inserir('Luiz Carlos', '883456')
    # agenda.inserir('José Luiz', '773456')
    # agenda.listar()
    # agenda.buscar('Luiz')
