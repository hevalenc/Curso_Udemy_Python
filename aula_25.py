#aula sobre desempacotamento de listas

# lista = ['Luiz', 'João', 'Maria']
# n1, n2, n3 = lista #a letra 'n' é uma variável, neste caso foram colocados 3 'n' porque a lista tem 3 valores

lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,7,8,9,100]
n1, n2, *outra = lista #neste caso, todos os valores restantes serão incorporados na variável descrita com '*'
n1, n2, *outra, ultimo = lista


print(ultimo)
