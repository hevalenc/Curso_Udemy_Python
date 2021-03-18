#aula sobre Combinations, Permutations e Product - itertools
"""
Combinação - ordem não importa
Permutação - ordem importa
Ambosnão repetem valores únicos
Produto - ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduaro', 'Letícia', 'Fabrício', 'Rosa']

# for grupo in combinations(pessoas, 2): #combinação de '2' valores da lista citada, a combinação 'Luiz' 'André' e
#     print(grupo)                       #'André' 'Luiz' serão considerados iguais, só terá um deles

# for grupo in permutations(pessoas, 2): #a combinação irá ocorrer igual ao anterior, porém 'Luiz' 'André' e 'André' 'Luiz'
#     print(grupo)                       #serão considerados diferentes, terá os dois

# for grupo in product(pessoas, repeat=2): #a combinação irá ocorrer igual ao anterior, porém 'Luiz' 'André' e 'André'
#     print(grupo)                         #'Luiz' serão considerados diferentes, terá os dois e terá 'Luiz' 'Luiz' porque
                                         #o 'product' permite repetir os valores

for grupo in combinations(pessoas, 3):
    print(grupo)