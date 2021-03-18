#aula sobre levantamento de exceções (raise)

# def divide(n1 , n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error: #tratando um erro previsto
#         print('Log: 'error)
#         raise #relançando uma exceção
#
# print(divide(2,0))

def divide(n1 , n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0') #o comando 'raise' pode ser usado para levantar um erro, neste exemplo,
                                              #o texto do erro será apresentado na tela em frente ao "ValueError"
    return n1 / n2

print(divide(2,0))