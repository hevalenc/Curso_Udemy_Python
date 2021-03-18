#aula sobre funções decoradoras e decoradores
"""
Este exemplo tem uma função escrava dentro de outra função que será a mestra, a mestra, no exemplo, vai executar uma
outra função externa
"""
# def master(funcao):
#     def slave(): #pode criar uma função dentro de outra função
#         funcao()
#     return slave
#
# @master #isto é um decorador
# def fala_oi():
#     print('Oi')
#
# master(fala_oi) #a função mestre irá executar a função fala_oi
#
# variavel = master(fala_oi) #a variavel vai decorar a função
#
# variavel()

from time import time, sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora() #a função demora vai funcionar com o decorador @velocidade