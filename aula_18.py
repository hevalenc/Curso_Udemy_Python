#aula sobre o comando 'while'
#a palavra 'continue'serve para pular um passo no loop 'while'
#a palavra 'break' serve para encerrar um loop

# x = 0 #coluna
# y = 0 #linha

# while x <= 10:
#     if x == 3:
#         x = x+1
#         continue
#     if x == 8:
#         break
#     print(x)
#     x = x + 1

# while x < 10:
#     y = 0
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
#         y += 1 #contador y + 1
#     x += 1

# print('Acabou a contagem')

while True:
    print('CALCULADORA')
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')#+, -, *, /
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador inválido')