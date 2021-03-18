#aula sobre Datetime - continuação

from datetime import datetime
from locale import setlocale, LC_ALL #este módulo permite formatar o idioma do programa
from calendar import mdays

setlocale(LC_ALL, '') #string vazia significa idioma local da máquina

data = datetime.now()
formatacao = data.strftime('%A, %d de %B de %Y') #formato de saída: Wednesday, 19 de August de 2020 - dia atual sem locale
                                                 #quarta-feira, 19 de agosto de 2020 com locale
print(data)
print(formatacao)

mes_atual = int(data.strftime('%m'))
print(mdays) #último dia de cada mês: [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(mes_atual,mdays[mes_atual]) #imprime o mês atual e qual é o último dia do mês