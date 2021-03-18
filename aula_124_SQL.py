#aula sobre SQLite - usando o módulo sqlite3 - o arquivo 'basededados.db' pertence a esta aula

import sqlite3

conexao = sqlite3.connect('basededados.db') #vai ser conectado uma base de dados ao arquivo
cursor = conexao.cursor() #esta linha de comando serve para navegar no banco de dados

#as informações com letras maiúsculas significam comandos
#toda vez que executar este programa, a linha abaixo será executada, por isto está comentado
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes(' #comando para inserir informações no banco de dados, criar uma tabela
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,' #gerar uma identificação com chave primária e automáticamente
#                'nome TEXT,' #o valor 'nome' recebe um texto
#                'peso REAL' #o valor 'peso' recebe um número real (pode ter números com ponto flutuante)
#                ')')
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Luiz",80.5)') #inserir os dados na tabela do banco de dados
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?,?)', ("Maria", 50)) #adicionando uma tupla
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome,:peso)', #adicionando valores usando dicionário
#                {'nome':'João', 'peso':25}
# )
#
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id':None, 'nome':'Daniel', 'peso':113}
# )

# cursor.execute('UPDATE clientes SET nome = :nome WHERE id = :id', #atualizar uma informação no banco de dados
#                {'nome':'Joana','id':2})

# cursor.execute('DELETE FROM clientes WHERE id = :id', #remover uma informação no banco de dados
#                {'id':2})

conexao.commit() #executar o comando cursor.execute criado acima

#toda vez que executar este programa, a linha abaixo será executada
# cursor.execute('SELECT * FROM clientes') #exibir todos os valores da base de dados clientes

# cursor.execute('SELECT nome, peso FROM clientes') #exibir valores definidos da base de dados clientes

# cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', #vai produzir o mesmo efeito do comando acima, porém
               {'peso':50})                                          #é o mais comum


for linha in cursor.fetchall():
    # print(linha) #exibir a informação em uma tupla '(1, 'Luiz', 80.5)' o número 1 é o id gerado pelo programa
    # identificador, nome, peso = linha
    # print(identificador, nome, peso)
    nome, peso = linha
    print(nome, peso)


cursor.close() #fechar o cursos no banco de dados
conexao.close() #fechar o banco de dados