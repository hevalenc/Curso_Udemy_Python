#aula sobre expressão condicional com operador 'OR'
#pode substituir a condição 'if' e simplificar o código de programação

# nome = input('qual é o seu nome: ')

# if nome:
#     print(nome)
# else:
#     print('você não digitou nada')

# print(nome or 'você não digitou nada') #se for verdadeiro exibe a variavel digitada, caso falso exibe a frase

a = 0 #retorna falso
b = None #retorna falso
c = False #retorna falso
d = [] #lista vazia #retorna falso
e = {} #dicionário vazio #retorna falso
f = 22 #retorna verdadeiro pq é diferente de zero
g = 'Luiz' #retorna verdadeira pq não é um vazio ou nada

variavel = a or b or c or d or e or f or g #esta expressão vai procurar um verdadeiro, conforme a sequência
print(variavel)