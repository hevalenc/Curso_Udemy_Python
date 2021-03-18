#aula sobre built-in Random - números aleatórios e mais

import random
import string

# Gerar um número inteiro entre A e B
inteiro = random.randint(10, 20)
print(f'Gera um número inteiro entre 10 e 20:               {inteiro}')

# Gerar um número aleatório usando a função range()
inteiro1 = random.randrange(900, 1000, 10)
print(f'Gera um número, múltiplo de 10, entre 900 e 1000:   {inteiro1}')

# Gera um número de ponto flutuante entra A e B
flutuante0 = random.uniform(10, 20)
print(f'Gera um número flutuante entre 10 e 20:             {flutuante0}')

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2) #o número 2 significa: 2 valores
print(f'Selecionar aleatóriamente dois nome da lista:       {sorteio}')
# sorteio1 = random.choices(lista, k=2)
# print(sorteio1)
sorteio2 = random.choice(lista)
print(f'Selecionar aleatóriamente um nome da lista:         {sorteio2}')

# Embaralha a lista
embaralha = random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
