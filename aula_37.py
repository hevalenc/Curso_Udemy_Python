#Exercícios

"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada
"""
print('Exercício 1')

def soma(n1,n2):
    return n1+n2

def calculando(funcao):
    return funcao

calculo = calculando(soma(2,3))
print(calculo)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1
executar duas funções que recebam um número diferente de argumentos.
"""
print('\nExercício 2')

lista = (1,2,3,4)

def funcao(funcao1, funcao2):
    return funcao

def funcao1():
    print(list(lista))

def funcao2():
    nova_lista = list(lista)
    nova_lista[0] = 20
    print(nova_lista)

funcao(funcao1(), funcao2())


print('\nExercício 2 - Professor')

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia')
print(executando)
print(executando2)