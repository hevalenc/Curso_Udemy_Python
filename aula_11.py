#aula sobre operadores relacionais ==, >, >=, <,<= e != (diferente)

nome = input('Qual é o seu nome: ')
idade = input('Qual é a sua idade: ')
idade = int(idade)
limite_1 = 20
limite_2 = 30

if idade >= limite_1 and idade <= limite_2:
    print(f'{nome} pode pegar um empréstimo.')
else:
    print(f'{nome} não pode pegar um empréstimo.')