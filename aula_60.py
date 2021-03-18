#aua sobre módulos padrão do Python
"""
Módulos são arquivos .py (que contém código python) e servem para expandir as funcionalidades padrão da linguagem.
Veja todos os módulos padrão do python em:
https://docs.python.org/3/py-modindex.html
"""

# import sys #importando o módulo 'sys' para sistema
#from sys import platform #importando somente a função especifica de um módulo

#verificar o sistema operacional do computador
# print(sys.platform) #o comando é usado desta forma "módulo.comando" quando se importa todo o módulo
# print(platform) #só é utilizado o comando quando se importa o comando do módulo

# from sys import platform as so #pode-se dar um nome ou apelido para um comando importado de um módulo
#
# print(so) #foi utilizado o apelido ao invés do comando

import random

print(random.randint(0,10)) #gerar um número aleatório entre 0 e 10