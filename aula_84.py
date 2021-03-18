#aula sobre Agregação - o arquivo classes1.py está associado a esta aula
#agregação é um tipo de associação onde uma classe depende de outra classe

from classes1 import CarrinhoDeCompra, Produto

carrinho = CarrinhoDeCompra()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 5000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)

carrinho.lista_produto()
print(carrinho.soma_total())