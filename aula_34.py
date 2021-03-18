#Exercícios
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""
print('Exercício 1')
def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Heitor')

"""
2 - Cre uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""
print('\nExercício 2')
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(1,2,3)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return)
o valor do primeiro número somado do aumento do percentual do mesmo.
"""
print('\nExercício 3')
def funcao(n1, n2):
    print(n1 + (n1*n2/100))

funcao(10,50)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por
5, retorne buzz. Se o parâmetro da função for divisível por 3 e por 5, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
print('\nExercício 4')
def jogo(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 ==0:
        return 'Buzz'
    else:
        return numero

var = jogo(30)
print(var)

