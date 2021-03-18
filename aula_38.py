#aula sobre expressões lambda - funções anônimas

# def funcao(arg1, arg2):
#     return arg1 + arg2
#
# var = funcao(2,2)
# print(var)

# esta função foi substituida pela expressão 'lambda' abaixo:

# a = lambda x, y: x * y
# print(a(2,2))

lista = [
    ['P1', 13],  #índice: P1 = 0, 13 = 1
    ['P2', 6],
    ['P3', 7],
    ['P5', 50],
    ['P4', 8],
]
# criando um método para ordenar as listas dentro da lista com uma função
# def func(item):
#     return item[1]
# print(lista)
# lista.sort(key=func) #a função foi a referência para ordenar os itens da lista por ordem crescente
# print(lista)

#usando o comando 'lambda' para ordenar as listas em ordem crescente
# lista.sort(key=lambda item: item[1])
# print(lista)

print(lista)
print(sorted(lista, key=lambda i: i[1])) #usando o índice 1 como referência
print(sorted(lista, key=lambda i: i[1], reverse=True))
print(sorted(lista, key=lambda i: i[0])) #usando o índice 0 como referência