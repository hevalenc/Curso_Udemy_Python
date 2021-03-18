#aula sobre estrutura de repetição com o comando 'for'
#while - usado para aquilo que não se sabe ou infinito
#for - usado para o quese sabe ou finito

# texto = 'Python'

# c = 0 #criar a condição
# while c < len(texto): #criar a expressão e tenho que conhecer os limites
#     print(texto[c])
#     c += 1

# for letra in texto: #este comando gera a mesma condição do loop 'while' acima
#     print(letra)

# for n, letra in enumerate (texto): #a função 'enumerate' enumera os laços do comando
#     print(n, letra)

# for numero in range(10): #contador simplificado
#     print(numero)

"""
Função range (start=0, stop, step=1)
"""

# for y in range(5, 10, 1): #inicio em 5 até 10, de 1 em 1 - contagem crescente, para no 9 (o 'stop' não é adicionado)
#     print(y)
# for x in range (20, 10, -2): #inicio em 20 até 10, de 2 em 2 - contagem decrescente, para no 11
#     print(x)

# for n in range(0,100, 8):
#     print(n)
#
# for n in range(100):
#     if n % 8 == 0: #'%' é o resto da divisão
#         print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)