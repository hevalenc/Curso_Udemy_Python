#aula sobre métodos de classe - métodos de instâncias

class Pessoa:
    ano_atual = 2019 #as variáveis citados abaixo da classe e fora de métodos são chamados de atributos da classe

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade) #nesta linha está usando um atributo da classe

    @classmethod #decorador que está decorando o método abaixo
    def por_ano_nascimento(cls, nome, ano_nascimento): #'cls' significa classe, deve ser usado somente em métodos
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('Luiz', 32)
# p1 = Pessoa.por_ano_nascimento('Luiz',1987)
print(p1)
print(p1.nome, p1.idade)

p2 = Pessoa('João', 25)

# print(p1.idade)
# p1.get_ano_nascimento()
# p2.get_ano_nascimento()

