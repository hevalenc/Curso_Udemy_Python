#aula sobre CRUD - CREATE, READ, UPDATE, DELETE com Pymsql no MySQL

import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()

# INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)' #'%s' representa o valor citado
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220)) #enviar somente uma linha de valor para ser inserido
#         conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]
#         cursor.executemany(sql, dados) #enviar várias linhas de  valores pra serem inseridos de uma só vez
#         conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# DELETA QUANTIDADE DETERMINADA DE REGISTROS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# DELETA REGISTRA ENTRE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         conexao.commit()

# ESTE SELECIONA OS DADOS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100') #'ASC' - ordenação ascendente, 'DESC' - descendente
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
