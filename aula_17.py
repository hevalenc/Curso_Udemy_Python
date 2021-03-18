# aula sobre manipulação de 'strings'
"""
String índices
Fatiamento de strings (início, fim, passo)
Funções built-in: len, abs, type, print, etc.
"""

#indice positivos   [012345678]
texto             = 'Python S2' #não é elegante deixar um espaço muito grnde em uma linha de comando
#indice negativos  -[987654321]
#neste exemplo: P=0, y=1, t=2, h=3, ......
print(f'{texto} tem {len(texto)} caracteres')
print(texto[2]) #todo número entre colchetes, neste caso, é usado para acessar o indice do texto, vai mostrar a letra

nova_string = texto[2:6] #fatiamento de uma string, neste caso foi dado o intervalo do fatiamento
nova_string1 = texto[:6]
nova_string2 = texto[-2]
print(nova_string, '//', nova_string1, '//', nova_string2)
nova_string3 = texto[0:8:2] #fatiamento de string com passo, foi dado o intervalo (os dois primeiros números) e o passo (terceiro)
nova_string4 = texto[0::2]
print(nova_string3, '//', nova_string4)

url = 'www.google.com.br/'
print(url[:-1])
print(url[4:10])
print(url.upper()[4:10])