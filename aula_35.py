#aula sobre funções 'def' - parte 3
#'args' - argumentos // 'kwargs' - key word args

#Quantidade definida de argumentos
# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
# #uma vez inserido os valores na função, deve-se manter o padrão e se alterar, o padrão na sequência, o novo pardrão deve ser usado
#     print(a1, a2, a3, a4, a5, nome, a6)

# def func(*args): #Quantidade não definida de argumentos, são empacotados em tupla
#     print(*args)
#     print(args[0])#mostar o primeiro
#     print(args[-1])#mostrar o último
#     print(len(args))
#
# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n) #o 'n'empacotou os números 3,4,5 na mesma lista
# print(*lista, sep='-')#o comando 'sep' foi utilizado para separar os valores da lista com o valor recebido
# func(1,2,3,4,5)

def func(*args, ** kwargs):
    # args = list(args)#conversão da tupla em lista
    # args[0] = 20
    print(args)
    print(kwargs)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Heitor', sobrenome='Valença')
#foi adicionado os elementos das duas listas em uma lista na função '*args'
#os números estão em args e os nome em kwargs
