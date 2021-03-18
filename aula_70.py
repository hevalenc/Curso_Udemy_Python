#aula sobre métodos estáticos

from random import randint

class Pessoa:
    ano_atual = 2019 #as variáveis citados abaixo da classe e fora de métodos são chamados de atributos da classe

    def __init__(self,nome, idade): #'self' é a instância
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade) #nesta linha está usando um atributo da classe

    @classmethod #decorador que está decorando o método abaixo, utiliza a instância da classe
    def por_ano_nascimento(cls, nome, ano_nascimento): #'cls' significa classe, deve ser usado somente em métodos
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod #não faz uso da instânica ou da classe
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Luiz', 32)
print(Pessoa.gera_id())
print(p1.gera_id()) #não será acessado a istância da classe