#aula sore Herança Simples - este arquivo está associado a aula_86
#a herança ocorre de cima para baixo, ou seja, a super classe (classe mão não herda funções de outras classes) e a
#sub-classe (classe filha) herda funções da super classe

class Pessoa: #esta classe é chamada de super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__ #nomear as classes que estão usando esta função

    def falar(self):
        print(f'{self.nomeclasse} falando ...')

class Cliente(Pessoa): #usará o mesmo método def __init__ da classe Pessoa, então instancia a classe origem entre ()
                       #em outra classe, isto é Herança, onde uma classe herda tudo de outra classe. Esta é uma sub-classe
    def comprar(self):
        print(f'{self.nomeclasse} comprando ...')

class Aluno(Pessoa): #sub-classe pode ter métodos específicos
    def estudar(self):
        print(f'{self.nomeclasse} estudando ...')
