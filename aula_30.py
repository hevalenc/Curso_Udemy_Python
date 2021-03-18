#aula sobre validador de CPF
"""
MÉTRICA USADA PELO PROFESSOR
CPF = 168.995.350-09
--------------------------------------------------------
->NESTA COLUNA USA-SE       -> NESTA COLUNA USA-SE
OS 9 PRIMEIROS NUMEROS      OS DOIS ÚLTIMOS

1 * 10 = 10                 1 * 11 = 11
6 * 9  = 54                 6 * 10 = 60
8 * 8  = 64                 8 * 9  = 72
9 * 7  = 63                 9 * 8  = 72
9 * 6  = 54                 9 * 7  = 63
5 * 5  = 25                 5 * 6  = 30
3 * 4  = 12                 3 * 5  = 15
5 * 3  = 15                 5 * 4  = 24
0 * 2  = 0                  0 * 3  = 0
           dígito gerado -> 0 * 2  = 0

Total  = 297                Total  = 343
11 - (297 % 11) = 11        11- (343 % 11) = 9
11 > 9 = 0
Digito 1 = 0                Digito 2 = 9
"""

while True:
    # cpf = '16899535009' #CPF referência para este código
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                     #Elimina os dois últimos digitos do CPF
    reverso = 10                            #Contador reverso
    total = 0
    for index in range(19):
        if index > 8:                       #Primeiro índice vai de0 a 9
            index -= 9                      #São os 9 primeiros dígitos do CPF

        total += int(novo_cpf[index]) * reverso     #Valor total da multiplicação

        reverso -= 1                        #Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                       #Se o digito for > que 9, o valor é 0
                d = 0
            total = 0                       #Zera o total
            novo_cpf += str(d)              #Concatena o dígito gerado no novo CPF

    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')