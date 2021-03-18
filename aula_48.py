#Exercícios
"""
Crie um carrinho de compra e adicione o produto com o preço (P,10), independente de quantidade. Use o list comprehension
"""
carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))

total1 = sum([y for x,y in carrinho])
print(total1)