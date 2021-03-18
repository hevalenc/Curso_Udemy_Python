#aula sobre 'SETS' (Conjuntos)
"""
add (adiciona), update (atualiza), clear, discard
union "|" (une)
intersection "&" (todos os elementos presentes nos dois sets)
difference "-" (elementos apenas no set da esquerda)
symmetric_difference "^" (elementos que estão nos dois sets, mas não em ambos)
"""
#os sets e os dicionários são construídos com chaves, porém nos sets não há chaves, só valores
#os sets não tem índice
#s1 = {1,2,3,4,5,6} se digitar s1={} será criado um dicionário vazio, para criar um conjunto vazio, usa-se set()
# s1 = set() #conjunto vazio
# s1.add(1)
# s1.add(2)
# s1.add((1,2,3,'Luiz'))
# print(s1)
#
# s1.discard(2)
# s1.update('Python') #é similar ao comando 'add', porém não respeita uma string e ordena as sílabas aleatoriamente no set
# print(s1)
#
# l1 = [1,2,1,1,3,4,5,6,6,6,6,'Luiz','Luiz']
# print(l1)
# l1 = set(l1)
# print(l1) #o conjunto não aceita valores duplicados
# l1 = list(l1)
# print(l1) #ao retornar o conjunto para a lista, os duplicados não irão retornar

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2 #o símbolo '|' significa união
s4 = s1 & s2 #o símbolo '&' significa intersecção, criar um conjunto com valores iguais nos dois conjuntos
s5 = s1 - s2 #o símbolo '-' significa só os itens da esquerda, criar um conj somente com os valores do conj da esquerda
s6 = s1 ^ s2 #o símbolo '^' significa itens diferentes, criar um conj com valores diferentes entre os dois conjuntos

print(s3)
print(s4)
print(s5)
print(s6)