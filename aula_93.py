#aula sobre Métodos Mágicos

"""
https://rszalski.github.io/magicmethods/
"""

class A:
    def __new__(cls, *args, **kwargs): #método mágico de construção que recebe atributos de instância
        cls.nome = 'Heitor'
        return super().__new__(cls)

    def __init__(self): #método mágico de inicialização e recebem os atributos de instância
        print('Eu sou o INIT')


a = A()
print(a.nome)