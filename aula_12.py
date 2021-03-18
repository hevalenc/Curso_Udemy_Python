#aula sobre operadores lógicos: and, or, not, in e not in

usuario = input("nome de usuário: ")
senha = input('digite a sua senha: ')

usuario1 = 'hevalenc'
senha1 = '12345'

if usuario == usuario1 and senha == senha1:
    print('você está logado no sistema')
elif usuario == usuario1 and senha != senha1:
    print('senha incorreta')
elif usuario !=usuario1 and senha == senha1:
    print('usuario inválido')
else:
    print('usuário e senha inválidos')