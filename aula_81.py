#aula sobre atributos de classe

class A:
    vc = 123

    def __init__(self): #o comando '__init__' é um inicializador ou construtor
        self.vc = 321

a1 = A()
a2 = A()

# a1.vc = 321 #está sendo alterado o valor da variável da classe
#
# print(a1.__dict__) #o comando '__dict__' é usado para evidenciar o valor de uma variável, o 'a1.' recebeu '321'
# print(a2.__dict__) #o 'a2.' não recebeu nada, mostrará um dicionário vazio
# print(A.__dict__) #o 'A.' possui diversas informações referentes a construção da classe

print(a1.vc)
print(a2.vc)
print(A.vc) #está sendo chamado a classe
