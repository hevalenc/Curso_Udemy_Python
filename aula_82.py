#aula sobre encapsulamento - utilizado para proteger o código

"""
Na  programação orientada o objetos (OOP)
public - os dados são públicos, ou seja, estão abertos para todos e pode ser modificado fora da classe
protected - os dados são protegidos e não podem ser alterados fora da classe, somente dentro do módulo, usa-se ( _ )
private - os dados ficam protegidos e não há como alterar fora da classe, usa-se ( __ )
No Python não há proteções claras, usa-se por convenção  '_'  e '__' em frente as variáveis significa não alterar
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rosa')
# bd.dados = 'Uma outra coisa' #esta linha de comando modificou o atributo '.dados' e sabota todo o programa
# bd.inserir_cliente(4, 'Ronaldo')

# bd.apaga_cliente(2)
# bd.lista_clientes()
# print(bd.dados)
