#aula sobre o uso dos comandos 'try' e 'except' como condicional

# numero = input('Digite um número: ')
# print(numero + 5) #vai ocorrer um erro pela tentativa de somar uma string comum inteiro
# print(numero * 5) #não vai ocorrer nenhum erro, porém será exibido 5 vezes o número digitado

def converte_numero(valor):
    try:
        valor = int(valor) #conversão do 'input' para inteiro
        return valor
    except ValueError: #se ocorrer um erro na conversão acima será dado o tratamento abaixo
        try:
            valor = float(valor) #nova tentativa para tratar um erro e corrigir a entrada
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is not None:
        print(numero * 5)
    else:
        print('Não é um número')
