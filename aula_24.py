#aula sobre os comandos 'split - dividir uma string', 'join - juntar uma lista', 'enumerate - enumerar elementos da lista'

string = 'O Brasil é o país do futebol , o Brasil é penta'
lista1 = string.split(' ')
lista2 = string.split(',')
print(lista1)
print(lista2)
# print()
# for valor in lista1:
#     print(f'A palavra "{valor}" apareceu {lista1.count(valor)}x na frase')
#     #o comando '.count' é um contador de palavras

# palavra = ''
# contagem = 0
# for valor in lista1:
#     qtd_vezes = lista1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

# for valor in lista2:
#     print(valor.strip().capitalize())
#     #o comando '.strip' remove os espaços, o '.capitalize' deixa só a primeira letra maiúscula

# lista = [#é possível ter várias listas dentro de uma lista
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
# for v in lista:
#     print(v)
"""
lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]
lista1 = ['Luiz', 'João', 'Maria']
for indice, valor in lista:
    print(indice, valor)
for indice, valor in enumerate(lista1):
    print(indice, valor)

n1, n2, n3 = lista1
print(n2)
"""