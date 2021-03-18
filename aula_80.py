#aula sobre @property - Getters e Setters

#Getter - obtém um valor
#Setter - configura um valor

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco* (percentual / 100))

    #Getter - é usado para capturar um atributo (variável) para ser trabalhado e pode ser usado para proteger o código
    #contra erros, tratando a variável sem modificar a estrutura do código

    @property #decorador de propriedade, usa-se property para Getter
    def preco(self):
        return self._preco #por convenção o novo nome para uma mesma variável é: '_variável'

    #Setter - é usado para configurar uma variável que pode obter um valor diferente do especificado (str, int, float)
    #e configurá-lo para o formato correto

    @preco.setter #usa-se o nome da propriedade (atributo) desejado
    def preco(self, valor): #a variável 'valor' irá receber o mesmo valor da variavel 'preco'
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    #outro exemplo para Getter e Setter:

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title() #utilizando o Setter para padronizar a formatação do nome dos produtos


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caneca', 'R$ 15')
p2.desconto(10)
print(p2.nome, p2.preco)