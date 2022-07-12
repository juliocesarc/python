lista = [
    ('chave', 1),
    ('chave2', 'valor2')
]

#print(dict(lista))

# ou

ex1 = {x: y for x, y in lista}
#print(ex1)

ex2 = {x: y for x, y in enumerate(range(5))}
print(ex2)