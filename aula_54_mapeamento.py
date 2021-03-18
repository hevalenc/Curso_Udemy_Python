#aula sobre mapeamento de dados
#o comndo 'map' serve para mapear uma função em uma lista ou dicionário

from aula_54_dados import produtos, pessoas, lista #foram importados as listas do arquivo

# nova_lista = map(lambda x: x*2, lista) #o comando 'map' retorna um iterador
# nova_lista = [x*2 for x in lista] #este list comprehension executa a mesma função acima
# print(lista)
# print(nova_lista)

# def aumenta_preco(p):
#     p['preço']= round(p['preço']*1.05, 2)
#     return p
#
# precos = map(lambda p: p['preço'], produtos) #o comando 'map' pede uma função entre ()
# for preco in precos:
#     print(preco)
#
# novos_produtos = map(aumenta_preco, produtos)
# for produto in novos_produtos:
#     print(produto)

def aumenta_idade(p):
    p['nova_idade']= p['idade'] * 1.20
    return p

# nomes = map(lambda p: p['nome'], pessoas)
# for pessoa in nomes:
#     print(pessoa)

nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)