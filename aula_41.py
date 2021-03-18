#aula sobre sistema de perguntas e respostas

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2?',
        'respostas': {'a': '1', 'b': '3', 'c': '5'},
        'resposta certa': 'b'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 310*0?',
        'respostas': {'a': '0', 'b': '310', 'c': '1'},
        'resposta certa': 'a'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 33/3?',
        'respostas': {'a': '3', 'b': '11', 'c': '99'},
        'resposta certa': 'b'
    }
}
print()
respostas_certas = 0
#pk = pergunta key     pv = pergunta value
#rk = respostas key    rv = respostas value
for pk, pv in perguntas.items():   #acessando o dicionário "key" 'pergunta' e o valor é a pergunta
    print(f'{pk}:{pv["pergunta"]}')
    print('Respostas: ')

    for rk,rv in pv['respostas'].items():  #acessando o dicionário "key" 'respostas' e o valor são as alternativas
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta certa']:
        print('!!! Acertouuuuuuuuu !!!')
        respostas_certas +=1
    else:
        print('### Errrroooouuuuuuuuu ###')
    print()

qtde_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtde_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua nota final é {porcentagem_acerto}%.')