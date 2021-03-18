#aula sobre built-in Datetime - https://docs.python.org/3/library/datetime.html

#strptime(str, fmt) - cria um objeto de data a partir de uma string
#.strftime(fmt)
#timestamp
#fromtimestamp

from datetime import datetime, timedelta

# data = datetime(2020, 8, 19, 20, 5, 00) #padrão de registro em programação: ano/mês/dia hora/minuto/segundo - 2020-08-19 20:05:00
# print(data)
# print(data.strftime('%d/%m/%Y %H:%M:%S')) #formato da saída: 19/08/2020 20:05:00
#
# data1 = datetime.strptime('20/08/2020', '%d/%m/%Y') #formato da saída: 2020-08-20 00:00:00, a hora não foi fornecida
# print(data1)
#
# data2 = datetime.fromtimestamp(1555729200.0) #formato de saída: 2019-04-20 00:00:00
# print(data2)

# data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# data = data + timedelta (days=5, seconds=59)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(dif.days)
print(dif.total_seconds())