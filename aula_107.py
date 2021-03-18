#aula sobre built-in JSON - o arquivo 'clientes.py' pertence a esta aula

"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas e programas muito leve e de fácil
utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""

from clientes import *
import json

lista = [1,2,3,4,5,6] #lista em python
dados_json = json.dumps(lista) #converter lista python em lista json - tipo array (string)
print(dados_json, type(dados_json))

# Converte um dicionário em JSON
# útil para salvar informações de qualquer tipo
dados = json.dumps(clientes_dicionario, indent=4)

# Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dados = json.loads(clientes_json)
print(dados)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as f:
    json.dump(clientes_dicionario, f, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as f:
    data = json.load(f)

print(data)
