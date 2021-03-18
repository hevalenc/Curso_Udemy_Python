#aula sobre criar módulos

import aula_61_calculos as calculos #este módulo foi criado por mim

# print(__name__) #este comando '__name__' chama '__main__'

print(calculos.PI)

lista = [2,4]
print(calculos.multiplica(lista)) #a lista entre () chama a variável lista
print(calculos.multiplica([2,5])) #a lista foi inserida entre os ()