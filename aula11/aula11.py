"""
listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

#append
animals = ['cat', 'dog', 'rours']
animals.append('pig')
print(animals)

#insert
frutas = ['maça', 'banana', 'melancia']
frutas.insert(1, 'morango')
print(frutas)

#pop
linguagens = ['python', 'java', 'c++', 'c']
retorna_valor = linguagens.pop(3)
print('retorna o valor:', retorna_valor)
print('lista:', linguagens)

#del
lista = [1, 2, 3, 4, 5, 6, 7, 8]
del lista[-1]
print(lista)

#clear
segunda_lista = [1, 2, 3, 4, 5, 6, 7, 8]
segunda_lista.clear()
print(segunda_lista)

#extend
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)

#range
l1 = list(range(10))
print(l1)

#