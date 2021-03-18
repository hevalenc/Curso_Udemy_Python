#aula sobre Groupby - agrupando valores

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota':'A'},
    {'nome': 'Letícia', 'nota':'B'},
    {'nome': 'Farício', 'nota':'A'},
    {'nome': 'Rosemary', 'nota':'C'},
    {'nome': 'Joana', 'nota':'D'},
    {'nome': 'João', 'nota':'A'},
    {'nome': 'Eduardo', 'nota':'B'},
    {'nome': 'André', 'nota':'A'},
    {'nome': 'Anderson', 'nota':'C'},
    {'nome': 'José', 'nota':'B'},
]
# alunos.sort(key= lambda item: item ['nota'])
ordena = lambda item: item ['nota'] #simplificação de código para evitar repetição
alunos.sort(key= ordena)
# print(alunos)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valore_agrupados in alunos_agrupados: #agrupamenta vai chamar o valor da chave nota
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valore_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')

# for aluno in valore_agrupados: #serão agrupados todos os valores conforme a chave acima citado
#     print(aluno)
