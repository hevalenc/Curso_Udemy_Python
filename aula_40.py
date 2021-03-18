#aula sobre dicionários - {}

# lista = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ] #se a lista possuir valores em pares, como no exemplo, pode-se converter em dicionário conforme abaixo
# d1 = dict(lista)
# print(d1)

d1 = {
    1:2,
    2:3,
    3:4
}
d2 = {
    'a':'b',
    'c':'d',
}
d1.update(d2) #concatenação de dicionários
print(d1)

# d1.pop(3) #o comando 'pop' é usado para remover uma chave do dicionário, se o () estiver vazio, remove-se a última chave
# print(d1)

# import copy
#
# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Heitor', 'Valenca']}
# v = copy.deepcopy(d1) #cópia profunda, função do built-in 'copy'
#
# v[1] = 'Luiz'
# v['d'][0] = 'Haed'
# #a alteração só ocorreu em 'v', devido a cópia profundo. O 'd1' permaneceu sem alteração
# print(d1)
# print(v)

# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Heitor', 'Valenca']}
# v = d1 #este método não cria uma variável com o dicionário, o 'igual' diz que as duas variáveis são iguais
# print(v == d1) #o resultado será True porque os dois são iguais
#
# v = d1.copy() #copiando o 'd1' em 'v' - cópia rasa
# v[1] = 'Luiz'#alterando o valor da chave 1, só o dicionário 'v' foi alterado
#
# print(v['d'][0]) #visualizar o índice zero da lista que está no dicionário na chave 'd'
# #se alterar o valor da lista em 'v', será alterado o valor da lista em 'd1', devido a cópia rasa
# print(d1)
# print(v)

# clientes = {
#     'cliente1' :{
#         'nome' : 'Luiz',
#         'sobrenome':'Otávio',
#     },
#     'cliente2' : {
#         'nome' : 'João',
#         'sobrenome': 'Moreira',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}') #visualizar as chaves do dicionário
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}') #visualizar os itens de cada sub-dicionário, o comando '\t' é para tabulação


# d1 = {'chave1':'valor da chave'} #método mais comum para criar dicionário
# d1['nova chave'] = 'valor da nova chave'
#
# print(d1['chave1'])

# d1 = dict(chave1 = 'valor da chave', chave2 = 'valor da outra chave')
#
# print(d1)

# d1 = {
#     'str':'valor',
#     123:'outro valor',
#     (1,2,3,4):'tupla'
# } #o dicionário suporta todos os tipos de valores

# d1['nomedachave'] = 'agora ela existe'
# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))

# del d1['str'] #remover um item do dicionário
# print(d1)

# print('str' in d1)
# print('str' in d1.keys()) #essa sentença é igual ao de cima, checando as chaves
# print('valor' in d1.values()) #essa sentença checa os valores
#
# print(len(d1)) #contagem de pares no dicionário

# for k in d1: #'k' significa 'keys' - visualizar as chaves
#     print(k)
# for v in d1.values(): #visualizar os valores da lista
#     print(v)
# for k in d1.items(): #visualizar os itens da lista - chave + valor
#     print(k)