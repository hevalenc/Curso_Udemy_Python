#aula sobre Filter, retorna True or False de acordo com a função selecionada

from aula_54_dados import produtos, pessoas, lista

# nova_lista = filter(lambda x: x>5, lista) #esta linha de comando é equivalente ao list comprehension abaixo
# nova_lista = [x for x in lista if x > 5]
# print(list(nova_lista))

# nova_lista = filter(lambda p: p['preço'] > 50, produtos)
# for produto in nova_lista:
#     print(produto)

# def filtra(produto):
#     if produto['preço'] > 50:
#         return True
#
# nova_lista = filter(filtra, produtos)
# for produto in nova_lista:
#     print(produto)

def  filtra(pessoa):
    if pessoa['idade'] < 18:
        return True

nova_lista = filter(filtra, pessoas)
for pessoa in nova_lista:
    print(pessoa)