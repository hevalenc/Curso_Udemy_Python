#aula sobre Metaclasses

"""
Em python tudo é um objeto, incluindo classes.
Metaclasses são as 'classes' que criam classes.
"""
class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr':'OI'}) #'type' - metaclasse; 'A' - nome da classe; '()' - namespace; '{}' - dicionário (valor)
                                     #'()' - recebeu a classe 'Pai"
a = A()
print(a.attr)
print(a.nome)
print(type(a))

class Meta(type): #'type' é uma Metaclasse
    def __new__(mcs, name, bases, namespace): #'mcs' signifia metaclasse
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace: #foi criado um método para proteger um atributo na classe A
            print(f'{name} tentou sobreescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_classe = 'valor A'

class B(A):
    attr_classe = 'valor B'

class C(A):
    attr_classe = 'valor C'

c =C()
print(c.attr_classe)

# #namespace = {'__module__': '__main__', '__qualname__': 'B'}
#
# class Meta(type):
#     def __new__(mcs, name, bases, namespace): #'mcs' signifia metaclasse
#         if name == 'A':
#             return type.__new__(mcs, name, bases, namespace)
#
#         if 'b_fala' not in namespace:
#             print(f'É preciso criar o método b_fala em {name}')
#         else:
#             if not callable(namespace['b_fala']):
#                 print(f'b_fala precisa ser um método e não um atributo em {name}')
#
#         return type.__new__(mcs, name, bases, namespace)
#
# class A(metaclass=Meta):
#     def fala(self):
#         self.b_fala()
#
# class B(A):
#     teste = 'valor'
#     # b_fala = 'wow'
#
#     def b_fala(self):
#         print('Oi')
