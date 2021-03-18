#aula sobre Sobrecarga de Operadores
"""
No Python, o comportamento dos operadores é definido pormétodos especiais.
Alterar o comportamento de operadores com classes definidas pelo usuário
"""

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self): #tratando a saída do módulo <__main__.Retangulo object at 0x00000155A8309FD0>
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other): #'self' representa o primeiro objeto e 'other' representa o segundo objeto
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other): #'__lt__' é menor que
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):  # '__gt__' é maior que
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other): #'__eq__' é igualdade
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

#não é possível somar ou subtrair os valores de x e de y entre objetos somente com os operadores lógicos, será necessário
#trabalhar com métodos, conforme demonstrado na classe acima

r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

# print(r1 + r2) #neste exemplo o 'self' é o r1 e o 'other' é o r2
r3 = r1 + r2

print(r3) #a saída foi: <__main__.Retangulo object at 0x00000155A8309FD0> antes do tratamento da saída
print(r3 > r1)
print(r3 < r1)
print(r1 == r2)