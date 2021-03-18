#aula sobre como criar pacotes e módulos

"""
Pacote é uma pasta que contém arquivos .py
Exemplo de importação de função de um módulo(arquivo.py):
    *** preco_com_aumento = aula_62_vendas.calc_preco.aumento(preco, 15)
                           "pasta(pacote).módulo(arquivo).função(def)"
"""

# import aula_62_vendas.calc_preco #para importar um módulo de um pacote é necessário colocar o nome da pasta '.' arquivo
#
# preco = 49.90
# preco_com_aumento = aula_62_vendas.calc_preco.aumento(preco, 15)
# # preco_com_aumento = aula_62_vendas.calc_preco.aumento(valor=preco, porcentagem=15) #valor e porcentagem são parâmetros da função
# print(preco_com_aumento)

from aula_62_vendas.calc_preco import aumento, reducao
from aula_62_vendas.formata import preco

preco1 = 49.90 #se a variavel tiver o mesmo nome de uma função importada, a função será sobregravada pela variavel
preco_com_aumento = aumento(valor=preco1, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(preco1, 15)
print(preco_com_reducao)
