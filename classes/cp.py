from classes.conta import Conta #classes.conta significa: pasta.arquivo de origem, desta forma será importado somente
                                #a classe deste arquivo citado

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()