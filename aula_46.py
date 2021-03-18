#aula sobre Dictionary Comprehension
#é similar ao List Comprehension

lista = [
    ('chave', 'valor'),
    ('chave1', 'valor1'),
]
d1 = {x:y for x,y in lista}
d2 = {x.upper():y.upper() for x,y in lista}
d3 = {x:y for x,y in enumerate(range(5))}
d4 = {x for x in range(5)} #este comando criou um conjunto
d5 = {f'chave_{x}': x**2 for x in range(5)} #o 'x' neste caso, será usado para key e value, o x**2 significa x elevado a 2


print(d1)
print(d2)
print(d3)
print(d4, type(d4))
print(d5)