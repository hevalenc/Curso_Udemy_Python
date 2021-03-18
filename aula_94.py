#aula sobre Context Manager - Criando e usando um gerenciador de contexto

#os dois métodos de abertura e fechamento de arquivo abaixo tem o mesmo comportamento

#1)
# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()

#2)
# with open('abc.txt', 'w') as arquivo:
#     arquivo.write('Algum acoisa')

"""
*** Classe para gerenciador de contexto - no exemplo para arquivo ***

class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo o arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu da classe')
        self.arquivo.close()

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
"""

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')