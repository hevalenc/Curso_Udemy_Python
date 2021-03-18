#aula sobre o comando 'while' - continuação com 'else'

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('Finalizou o contador')
    #o comando 'else' só vai rodar quando o loop 'while' finalizar, se houver uma quebra do loop, este comando
    #não será executado