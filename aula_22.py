#aula sobre listas em Python

"""
fatiamento
append, insert, pop, del, clear, extend, +
min, max, range
"""
# lista = ['A', 'B', 'C', 'D', 'E', 10]
# print(lista)
# print(lista[0:3])
# print(lista[3:])
# print(lista[::2])
# print(lista[::-1])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l1, l2)

# l3 = l1 + l2 #concatenação simples
# print(l1, l2, l3)

# l1.extend(l2) #adicionando a lista 'l2' na'l1'

# l2.append('b') #adicionando um novo valor na lista, será o último

# l2.insert(0, 'a') #o primeiro valor indica a posição em que será inserido o novo valor
# print(l1, l2)

# l2.pop(1) #foi removido um item da lista, se não tem valor dentro do () será removido o último valor
# print(l2)

# lista = [10, 2, 3, 4, 5, 6, 70, 8, 9]
# print(lista)

# del(lista[3:5]) #remoção de itens na lista
# print(lista)

# print(max(lista)) #mostrar o maior valor
# print(min(lista)) #mostrar o menor valor

# lista1 = list(range(0, 10)) #o comando 'list' é um built-in gerador de lista
# print(lista1)

# l4 = ['string', True, 10, -20.5]
#
# for elem in l4:
#     print(f'O tipo de elem é{type(elem)} e seu valor é {elem}')


secreto = 'perfume'
digitadas = []
chances = 3
print('JOGO DA FORCA - 3 CHANCES')

while True:
    if chances == 0:
        print('Você perdeu!!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!!!!!')
        continue
    digitadas.append(letra)
    print(digitadas)

    if letra in secreto:
        print('A palavra secreta tem esta letra!!!')
    else:
        print('A letra não faz parte da palavra secreta!!!')

    temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            temporario += letra_secreta
        else:
            temporario += '*'

    if temporario == secreto:
        print(f'Você ganhou, a palavra secreta é "{temporario}"')
        break
    else:
        print(temporario)
    if letra not in secreto:
        chances -= 1
    print(f'Você em {chances} chances. \n')
