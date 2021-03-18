#exercício com estrutura de repetição

"""
for / while
0  10
1  9
2  8
3  7
4  6
5  5
6  4
7  3
8  2
"""
# numero = 0
# numero1 = 10
# while numero <= 8:
#     print(numero)
#     numero += 1
#
# while numero1 >= 2:
#     print(numero1)
#     numero1 -=1

# for numero in range(9):
#     print(numero)
#
# for numero1 in range(10, 1, -1):
#     print(numero1)

"""
SOLUÇÃO DO PROFESSOR PARA CONTADOR
"""
for p, r in enumerate(range(10,1,-1)):
    print(p, r)