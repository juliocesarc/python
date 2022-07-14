carrinho = []

carrinho.append(('Porduto 1', 30))
carrinho.append(('Porduto 2', 20))
carrinho.append(('Porduto 3', 50))
carrinho.append(('Porduto 4', 10))
carrinho.append(('Porduto 5', 70))
carrinho.append(('Porduto 6', 80))
carrinho.append(('Porduto 7', 20))

total = sum([produtos[1] for produtos in carrinho])
print(total)