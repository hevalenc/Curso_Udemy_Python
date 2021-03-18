#aula sobre Herança Múltipla - este arquivo pertence a aula_89

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('Saldo precisa ser numérico')

        self._saldo = valor

    def depositar(self,valor):
        if not isinstance(valor, (int,float)):
            raise ValueError('Valor do depósito precisa ser numérico')

        self.saldo += valor
        self.detalhes()

    @abstractmethod #o método abaixo não executará nada, porém deverá ser importado por uma outra classe
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')