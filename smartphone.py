#aula sobre Herança Múltipla - este arquivo pertence a aula_88

from eletronico import Eletronico
from log import LogMixing


class Smartphone(Eletronico, LogMixing): #exemplo de herança múltipla, primeiro é verificado o comando da classe instanciado
                                         #a esquerda e depois vai para a direita
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está conectado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if self._conectado:
            error = f'{self._nome} não está conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está desconectado'
        print(info)
        self.log_info(info)
        self._conectado = False
