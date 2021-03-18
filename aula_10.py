#aula sobre condições 'if', 'elif' e 'else'

numero = input('digite um número: ')

if int(numero) < 5:
    print('número é menor que 5')

elif int(numero) == 5:
    print('número é igual a 5')

else:
    print('número é maior que 5')