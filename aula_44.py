#aula sobre 'List Comprehension'
#usado para otimização de código

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1] #criação de uma lista
ex2 = [v * 2 for v in l1] #criação de uma lista com números multiplicados
ex3 = [(v,v2) for v in l1 for v2 in range(3)] #criando uma tupla com uma variável (v) de uma lista e criando uma nova
                                             #variável (v2) em uma range de 3, em duplas. O primeiro 'for' itera a lista
                                             #e o segundo 'for' itera os valores - ex: (1,0), (1,1), (1,2), (2,0) .....

l2 = ['Luiz','Mauro','Maria']
ex4 = [v.replace('a','@') for v in l2] #criando uma lista trocando um caracter da lista referência
ex5 = [v.replace('a','@').upper() for v in l2] #criando uma lista igual ao de cima com letras maiúsculas

tupla = (
    ('chave','valor'),
    ('chave2','valor2')
)
ex6 = [(y,x) for x,y in tupla] #criando uma nova tupla invertendo os valores
ex6 = dict(ex6) #convertendo a tupla em dicionário

l3 = list(range(100)) #criando uma lista com 100 números conforme indicado no ()
ex7 = [v for v in l3 if v % 2 == 0] #criando uma lista com números divisiveis por 2
ex8 = [v for v in l3 if v % 3 == 0 if v % 8 == 0] #criando uma lista com números divisiveis por 3 e por 8
ex9 = [v if v % 3 ==0 else 'Não é' for v in l3] #criando uma lista onde serão mostrados os números divisiveis por 3 e
                                                #será mostrado a string para os que não são divisiveis por 3
ex10 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3] #criando uma lista onde serão mostrados os números divisiveis
                                                           #por 3 e 8 e será mostrado 0 para os que não são divisiveis
