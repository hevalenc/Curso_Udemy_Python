#aula sobre Sobreposição de membros - este arquivo está associado a aula_87

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando ...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando ...')

    def falar(self):
        print('Estou em Cliente') #sobreposição

class ClienteVIP(Cliente): #cadeia de herança - 'ClienteVip' herda 'Cliente' que herda 'Pessoa'

    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade) #chamando o método da classe 'Pessoa'
        self.sobrenome = sobrenome #criei um novo atributo para a classe 'ClienteVip'

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

    # def falar(self): #este método sobrepõe o método 'falar' da classe 'Pessoa'
    #     # super(ClienteVIP, self).falar() #o comando ' super' chama o método da classe citado em () nesta classe
    #                                     #ou de outra classe
    #     Pessoa.falar(self) #outro modo para chamar um método de outra classe
    #     Cliente.falar(self)
    #     print(f'{self.nomeclasse} reclamando ...')
