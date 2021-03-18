#aula sobre formatação de valores com modificadores
"""
:s - texto (string)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^
"""
print('Exemplos de formatação\n')
num1 = 10
num2 = 3
divisao = num1 / num2
#print('{:.2}'.format(divisao)) #modo 1
print(f'Número de casas decimais na divisão: {divisao:.2f}') #modo 2
num3 = 1
num4 = 9581
print(f'Conversão para float com preenchimento: {num3:0>10.2f}')
print(f'Preenchimento de digitos a esquerda: {num3:0>10}')#o número '10' indica o total de casas do número
print(f'Preenchimento de digitos a direita : {num4:0<10}')
num5 = 998899
print(f'Preenchimento de digitos com o numero no centro: {num5:0^10}')

nome = 'Heitor Valenca'
print(f'{nome} tem {len(nome)} caracteres')
print(f'Preenchimento com "*" para ter 20 caracteres e centralizar o nome: {nome:*^20}')
#pode trocar o '*' por outro símbolo, espaço, letra ou número

print('\nOutros exemplos de formatação')
nome1 = nome.ljust(20, '#')
print(f'Centralizar a esquerda com ".ljust": {nome1}')
nome2 = nome.rjust(20, '$')
print(f'Centralizar a direita com ".rjust": {nome2}')
nome3 = nome.lower()
print(f'Escrever o nome com letras minúsculas com ".lower": {nome3}')
nome4 = nome.upper()
print(f'Escrever o nome com letras maiúsculas com ".upper": {nome4}')

nome5 = 'casa amarela'
print(nome5)
print(f'Escrever as primeiras letras com maiúsculas: {nome5.title()}')