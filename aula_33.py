#aula sobre funções 'def' - parte 2

# def funcao(var):
#     # print(var)
#     return var
#     print('não será executado devido ao comando return')
# variavel = funcao('valor que eu quero')
# # print(variavel) #ao final do programa será retornado o valor 'None' - significa nada
#
# if variavel:
#     print(variavel)
# else:
#     print('nenhum valor')
# #o programa vai rodar o código, como não tem o comando 'return' na função, será retornado ao final o comando 'else'
# #quando a função encontrar o comando 'return', ela retorna a condição inicial

def divisao(n1, n2):
    if n2 == 0:
        return #o 'return' pode ser usado para retornar um valor de qualquer tipo

    return n1 / n2

divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('conta inválida')
