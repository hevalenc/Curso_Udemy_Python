#aula sobre Deque - trabalhando com LIFO e FIFO

"""
Pilha (stack) - LIFO - last in, first out   #o último que entra será o primeiro a sair#
    Exemplo: pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out   #o primeiro que entra será o primeiro a sair#
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)

Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices serão modificados.
"""
#exemplo de pilha
livros = list()
livros.append('Livro 1')    #+1.
livros.append('Livro 2')    #+2.
livros.append('Livro 3')    #+3.
livros.append('Livro 4')    #+4.
livros.append('Livro 5')    #+5.
print(livros)
livro_removido = livros.pop() #-5.
print(livro_removido)
print(livros)
livro_removido = livros.pop() #-4.
print(livro_removido)
print(livros)

#exemplo de fila
from collections import deque #esta função permite remover itens da lista sem causar problemas com o índice

fila = deque()
fila.append('João')
fila.append('Maria')
fila.append('Luiz')
fila.append('Marcos')
fila.append('José')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

for nome in fila:
    print(nome)

fila1 = deque(maxlen=5) #'maxlen' - tamanho máximo da fila da lista
fila1.extend([1,2,3,4])
fila1.append(5)
print(fila1)
fila1.append(6)
print(fila1, 'Entrou o número 6')
fila1.append(7)
print(fila1, 'Entrou o número 7')

from time import sleep

fila2 = deque(maxlen=10)

for i in range(50):
    fila2.append(i)
    sleep(1)
    print(fila2)

