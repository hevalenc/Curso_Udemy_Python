#aula sobre trocar valores entre variáveis

x = 10
y = 'Luiz'
z = 'carro'
print(x, y, z)

x, y = y, x
print(x, y, z)

x, y, z = y, z, x
print(x, y, z)