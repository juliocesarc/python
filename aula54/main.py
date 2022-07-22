from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camisa', 40)
p2 = Produto('Iphone', 3500)
p3 = Produto('Caneca', 25)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()
print(carrinho.soma_total())