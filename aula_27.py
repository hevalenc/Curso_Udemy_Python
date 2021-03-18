#aula sobre operador ternário

# logged_user = False
# if logged_user: #sempre a primeira condição do comando 'if' é  checar a condição verdadeiro
#     msg = 'usuário logado'
# else:
#     msg = 'usuário precisa logar'

# msg = 'usuário logado' if logged_user else 'usuario precisa logar'
# #é possível colocar a condição na mesma linha de programação
#
# print(msg)

idade = input('Qual é a sua idade: ')
# if idade >= 18:
#     print('pode acessar')
# else:
#     print('não pode acessar')
if not idade.isnumeric():
    print('você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'pode acessar' if e_de_maior else 'não pode acessar'
print(msg)