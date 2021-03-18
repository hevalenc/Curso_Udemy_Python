#aula sobre Classes - Python Orientado a Objetos - arquivo pessoa.py pertence a esta aula

from pessoa import Pessoa #foi importado um módulo do arquivo pessoa.py

#as pessoas abaixo são objetos deste programa, também chamados de instâncias
p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

#abaixo tem ações importados do módulo pessoa, usando os métodos da classe 'Pessoa'

p1.comer('maçã') #executando o método do módulo 'pessoa', o 'self' será a pessoa mencionada entre () no p1 eo alimento foi
                 #informado, neste exemplo foi a maçã
p2.comer('sorvete')
p1.parar_comer()
p1.parar_comer() #as ações do método '_comer' são diferentes conforme descrito no módulo 'pessoa'
p1.falar('POO') #a execução é similar ao método'_comer', porém com outra ação, neste caso 'falar'
p1.parar_falar()
p1.comer('maçã')
p2.parar_comer()
p1.falar('POO') #como a condição do módulo é verdadeiro para '_comer' será informado que não pode falar comendo

print(p1.ano_atual) #este comando está usando um método do módulo 'pessoa'
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())