#aula sobre Associação - o arquivo classes.py pertence a esta aula
#uma classe utiliza outra classe diferente sem estar ligadas

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta #associação de métodos entre classes, escritor.ferramenta recebeu o método caneta para executar
escritor.ferramenta.escrever() #um método de uma classe executando um método de outra classe, associação simples

