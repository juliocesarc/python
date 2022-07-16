from dados import pessoas, lista, produtos

# Map

"""
#nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]
print(list(nova_lista))
"""
"""
a função map retona um iterador, sendo assim não é simplesmente dar um print,
devo adicionar a uma lista
"""

"""
def percentual(p):
    p['preco'] = round(p['preco'] + p['preco'] * (5 / 100), 1)
    return p

novos_produtos = map(percentual, produtos)

for produtos in novos_produtos:
    print(produtos)
"""
"""
iterador_com_nomes = map(lambda p: p['nome'], pessoas)

print(list(iterador_com_nomes))
"""

# Filter

"""
nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))
"""

"""
produtos_10 = filter(lambda p: p['preco'] > 10, produtos)
for prod in produtos_10:
    print(prod)
"""
"""
obj_com_dMaior = filter(lambda ind: ind['idade'] >= 18, pessoas)
for pessoa in obj_com_dMaior:
    print(pessoa)
"""

# Reduce

from functools import reduce

"""
soma_lista = reduce(lambda ac, ind: ac + ind, lista, 0)
print(soma_lista)
"""
"""
soma_produtos = reduce(lambda ac, ind: ac + ind['preco'], produtos, 0)
print(round(soma_produtos / len(produtos), 2))
"""

soma_idades = reduce(lambda ac, ind: ac + ind['idade'], pessoas, 0)
print(soma_idades / len(pessoas))