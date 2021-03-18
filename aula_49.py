#aula sobre Zip e Zip longest
"""
Zip - unindo iteráveis
Zip_longest - Itertools (built-in)
"""
from itertools import zip_longest, count #importando uma função do built-in, se importar só o built-in será necessário
                                         #citar o built-in antes do comando. Ex.: itertools.zip_longest

### Código
indice = count() #contador
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG','BA']

cidades_estados = zip(estados,cidades) #une até a menor lista
cidades_estados1 = zip_longest(estados,cidades) #une até a maior lista, se não tiver como formar mais pares usando
                                                #as duas listas, irá ser formado uma lista com 'None'
cidades_estados2 = zip_longest(estados,cidades, fillvalue= 'Estado') #o comando 'fillvalue' é usado para preencher
                                                                     #os valores vazios ('None') e formar os pares
#se utilizar o zip_longest com o count, será gerado uma lista infinita

cidades_estados3 = zip(indice, estados, cidades)

print(list(cidades_estados))
print(list(cidades_estados1))
print(list(cidades_estados2))

for indice, estados, cidades in cidades_estados3:
    print(indice, estados, cidades)