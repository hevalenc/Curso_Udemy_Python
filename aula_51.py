#aula sobre contadores infinitos 'count - itertools'

from itertools import count

# contador = count()

# print(next(contador)) #o contador derá apena um número
# print(next(contador))
# print(next(contador))
# print(next(contador))

# for valor in contador: #o loop for será infinito porque o 'count' é infinito
#     print(valor)
#
#     if valor >= 10: #aqui foi colocado um limitador para o loop for
#         break

# contador = count(start=5,step=0.001)
# contador = count(start=8, step=-1) #contador decrescente, devido ao step ser igual a um número negativo
#
# for valor in contador:
#     print(round(valor, 2)) #o comando 'round' serve para arredondar valores e foi solicitado para arredondar com 2 casas
#                            #decimais, no caso do exemplo
#     if valor >=10:
#         break

contador = count()
lista = ['Luiz', 'João', 'Maria', 'José', 'Silva', 'Eduardo']

lista = zip(contador, lista) #o contador está sendo utilizado como gerador de indíce
print(list(lista))