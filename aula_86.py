#aula sobre Herança Simples - o arquivo classes3.py está associado a esta aula
"""
Associação - Usa outra classe / Agregação - Tem outra classe / Composição - É donade outra classe / Herança - É a outra classe
"""

from classes3 import * #o * significa tudo

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()
#c1.estudar() não funciona porque não pertence a classe Cliente, c1 recebeu a classe filha Cliente
print()

a1 = Aluno('Maria', 50)
print(a1.nome)
a1.falar()
a1.estudar()
#a1.comprar() não funciona porque não pertence a classe Aluno, a1 recebeu a classe filha Aluno

p1 = Pessoa('João', 43)
p1.falar()
#p1.estudar() ou p1.comprar não funcionam porque o p1 recebeu a classe mãe Pessoa, nesta classe não está instanciada
#estes métodos