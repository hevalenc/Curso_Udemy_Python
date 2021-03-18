#aula sobre documetação e built-in

#o comando 'isnumeric' verifica se o valor inserido pode ser convertido em 'int'
#o comando 'isdigit' verifica se o valor inserido é um dígito

num1 = input('digite um número: ')
num2 = input('digite um número: ')

print(num1.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não foi possível converter para número')