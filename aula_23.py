#aula sobre os comandos 'for' e 'else'

variavel = ['Luiz', 'Joãozinho', 'Maria']

# for valor in variavel:
#     if valor.startswith('J'): #o comando '.startswith' verifica se o valor começa com o caractere dentro de ()
#         print(valor, ' : começa com J')
#     else:
#         print(valor, ' : não começa com J')

# comeca_com_j = False
# for valor in variavel:
#     if valor.startswith('J'):
#         comeca_com_j = True #nesta linha se altera o valor booleano da variavel 'comeca_com_j'
# if comeca_com_j:
#     print('Existe uma palavra com "J".')
# else:
#     print('Não existe uma palavra com "J".')

for valor in variavel:
    if valor.startswith('J'):
        continue
    print(valor)
