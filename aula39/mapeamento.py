from dados import pessoas, lista, produtos

#nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]
print(list(nova_lista))

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

iterador_com_nomes = map(lambda p: p['nome'], pessoas)

print(list(iterador_com_nomes))