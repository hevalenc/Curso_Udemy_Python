#Exercícios

"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

print('Execício 1')
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('Este é um número par')
    else:
        print('Este é um número ímpar')
else:
    print('Não foi digitado um número válido')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
print('\nExercício 2')
hora = input('Digite a hora sem os minutos: ')

if hora.isnumeric():
    hora = int(hora)
    if hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Digite entre 0 a 23')
else:
    print('Não foi digitado uma hora válida')

"""
Faça um programa que peça o primeiro nome de usuário. Se o nome tiver 4 letras ou menos, escreva: "Seu nome é
curto"; se tiver 5 e 6 letras, escreva: "Seu nome é normal"; maior que 6 letras, escreva:"Seu nome é muito grande"
"""

print('\nExercício 3')
usuario = input('Digite um nome de usuário: ')
usuario = len(usuario)

if usuario <= 4:
    print('Seu nome é curto')
elif usuario <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
