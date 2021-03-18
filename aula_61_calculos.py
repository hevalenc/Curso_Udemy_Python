#aula sobre criar módulos

import math

PI = math.pi #nomes de variáveis com maiúsculas são chamadas de constantes e não mutáveis

def dobra_lista(lista): #dobrar a lista
    return [x*2 for x in lista] #i - index

def multiplica(lista):
    r = 1 #r - resultado
    for i in lista:
        r *= i
    return r


# print(__name__) #ao usar este comando, ao rodar este arquivo como módulo em outro arquivo, o nome do arquivo irá aparecer

if __name__ == '__main__': #este bloco não irá ser executado em outro arquivo quando importado por outro
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
