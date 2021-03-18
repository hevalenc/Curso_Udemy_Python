#aula sobre Geradores, Iteradores e Iteráveis

# lista = [0,1,2,3,4,5] #é um conjunto iterável
# lista1 = 12345 #não é iterável
# lista2 = 'string' #é iterável
#
# print(hasattr(lista, '__iter__')) #built-in 'hasattr' é usado para ver a atribuição (ex.:'__iter__') e retorna True or False

# for v in lista: #é um iterador porque está trabalhando com o valor iterável, ou seja, tem um método next (próximo)
#     print(v)

import sys
import time

# #gerador
# def gera():
#     for n in range(100):
#         yield n #este comando é um gerador
#         time.sleep(0.1)
#
# g = gera()
#
# for v in g:
#     print(v)

l1 = [x for x in range(1000)] #a lista entrega todos os valores armazenados
print(type(l1))
l2 = (x for x in range(1000)) #o gerador só gera e entrega os valores quando solicitado
print(type(l2))

print(sys.getsizeof(l1)) #'getsizeof' é um comando do built-in 'sys' e serve para obter o tamanho do parametro na memória
print(sys.getsizeof(l2))
