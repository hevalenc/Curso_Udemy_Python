"""
O banco que você trabalha sempre tem problemas para organizar as filas de atendimento dos clientes.

Após uma reunião com a gerência ficou decidido que os clientes ao chegar na agência receberão uma senha numérica em seu
aparelho de celular via sms e que a ordem da fila será dada não pela ordem de chegada, mas sim pelo número recebido via
sms. Sendo, aqueles com número maior deverão ser atendidos primeiro.

Então, dada a ordem de chegada dos clientes reordene a fila de acordo com o número recebido via sms, e diga quantos
clientes não precisaram trocar de lugar nessa reordenação.
"""

sequencia = []

while:
    entrada = input('Entre com os números: ')
    if entrada != ' ':
        lista_entrada = entrada.split(' ')
        sequencia.append(lista_entrada)
    else:
        break


print(entrada)
print(lista_entrada)
print(sequencia)

