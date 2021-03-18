#aula sobre criar, ler, escrever e apagar arquivos
#https://docs.python.org/3/library/functions.html#open
"""
file = open('abc.txt', 'w+')
file.write('Linha 01\n')
file.write('Linha 02\n')
file.write('Linha 03\n')

file.seek(0,0) #este comando serve para mandar o cursor para o topo, porque o cursor, no python, fica na última linha do programa
print('Lendo linhas:')
print(file.read()) #ler todo o arquivo
print('*************')

file.seek(0,0)
print(file.readline()) #ler uma linha
print(file.readline(),end='') #o comando 'end' indica como terminará a linha, removendo a quebra de linha do arquivo
print(file.readline(),end='*')
print()

file.seek(0,0)
print(file.readlines()) #mostrará as linhas do arquivo em uma lista
print()

file.seek(0,0)
for linha in file.readlines(): #desempacotando um arquivo com .readlines e iterando-os
    print(linha)

file.close()
"""
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0.0)
#     print(file.read())
# finally:
#     file.close()


"""
'r' - open for reading (default)
'w' - open for writing, truncating the file first
'x' - open for exclusive creation, failing if the file already exists
'a' - open for writing, appending to the end of the file if it exists
'b' - binary mode
't' - text mode (default)
'+' - open for updating (reading and writing)
"""
# with open('abc.txt', 'w+') as file: #modo correto para python de abertura de arquivo
#     file.write('Linha 01\n')
#     file.write('Linha 02\n')
#     file.write('Linha 03\n')
#
#     file.seek(0)
#     print(file.read())
#
# with open('abc.txt', 'r') as file:
#     print(file.read())

# with open('abc.txt', 'a+') as file:
#     file.write('Nova linha\n')
#
#     file.seek(0)
#     print(file.read())

# import os
# os.remove('abc.txt') #remoção de arquivos

import json

d1= {
    'Pessoa 1': {'nome':'Luiz','idade':25},
    'Pessoa 2': {'nome': 'Rose', 'idade': 30},
}

d1_json= json.dumps(d1, indent=True)

# with open('abc.json', 'w+') as file:
#     file.write(d1_json)

# print(d1_json)

with open('abc.json','r') as file:
    d1_json= file.read()
    print(d1_json)
    d1_json = json.loads(d1_json) #converter os dados do json em dicionário
    print(d1_json)

for k,v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)