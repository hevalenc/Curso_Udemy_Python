#introdução a formatação de 'strings'

nome = 'Heitor'
idade = 39
altura = 1.71
peso = 90.2
maior = idade > 18
imc = peso / (altura ** 2)
imc_1 = imc > 18.50 and imc < 24.99

print(nome, 'tem', idade, 'anos e seu imc é', imc)
print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')
#o comando '.2f' significa 2 casas de pontos flutuantes (casas decimais)
print('{} tem {} anos e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
