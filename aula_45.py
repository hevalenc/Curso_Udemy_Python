#Exercícios
"""
Faça uma lista separando em grupos de 0 a 9 a string abaixo usando o List Comprehension
Retorne os grupos em uma string, onde cada grupo de 0 a 9 estajam separados por (.)
Ex.: string = '01234567890123456789'
     lista = ['0123456789','0123456789']
     retorno = '0123456789.0123456789'
"""
string = '01234567890123456789012345678901234567890123456789'
n = 10
lista=[string[i:i+n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)


print(lista)
print(retorno)