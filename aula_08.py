#atividade prática

"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Heitor'
idade = 40
altura = 1.71
peso = 90
ano_atual = 2020
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print('{} tem {} anos, tem {}m de altura e pesa {}Kg.'.format(nome, idade, altura, peso))
print('O IMC de {} é: {:.2f}'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, ano_nascimento))

print(f'{nome} tem {idade} anos, tem {altura}m de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é: {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}.')

print(f'{nome} tem {idade} anos, tem {altura}m de altura e pesa {peso}Kg. \nO IMC de {nome} é: {imc:.2f} \n{nome} nasceu em {ano_nascimento}.')