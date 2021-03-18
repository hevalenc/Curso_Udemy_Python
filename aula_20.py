#aula sobre a "iteração" de string com o comando 'while'

#índice  0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma' #Iterável
tamanho_frase = len(frase)
# print(tamanho_frase)
contador = 0
nova_string = ''

entrada = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase: #Iteraçãod
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == entrada:
        nova_string += entrada.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)