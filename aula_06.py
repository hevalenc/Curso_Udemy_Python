#aula sobre variáveis

nome = 'Heitor'
idade = 39
altura = 1.71
peso = 90.2
maior = idade > 18
imc = peso / (altura ** 2)
imc_1 = imc > 18.50 and imc < 24.99

print('Nome: ', nome, type(nome))
print('Idade: ', idade, type(idade))
print('Altura: ', altura, type(altura))
print('Peso: ', peso, type(peso))
print('Pode beber: ', maior, type(maior))
print('IMC: ', imc)
print('IMC ideal: ', imc_1)

