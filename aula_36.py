#aula sobre funções 'def' - parte 4

variavel = 'valor' #escopo global

# def func():
#     print(variavel)
#
# # def func2():
# #     global variavel#com este comando 'global' estou dizendo que a variavel pode ser editada pela função
# #     variavel = 'outro valor'#escopo local
# #     print(variavel)
#
# def func2(arg=None):
#     arg = arg.replace('v', 'c')#edição do argumento, o comando 'replace' troca as letras
#     return arg
#
# func()
# outra_variavel = func2(arg=variavel)
# print(outra_variavel)

def func():
    # print(variavel) #não é possível mesclar uma variavel global com a local quando tem o mesmo nome
    variavel = 1234
    print(variavel)

func()