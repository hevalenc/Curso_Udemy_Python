#aula sobre tuplas

# t1 = (1,2,3, 'a','Luiz')
# for v in t1:
#     print(v)

# t1 = 1,2,3,'a', 'Luiz'
# print(type(t1))

t1 = 1,2,3,4,5
t2 = 6,7,8,9,10
t3 = t1 + t2
# n1, n2, n3, *_ = t3 #desempacotando a tupla
# print(n1)

t1 = list(t1) #convertendo a tupla em lista
t1[1] = 3000
t1 = tuple(t1) #convertendo a lista em tupla
print(t1)
