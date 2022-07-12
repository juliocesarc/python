from operator import invert


l1 = list(range(100))
ex1 = [numero for numero in l1 if numero % 2 == 0]
#print(ex1)

l2 = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex2 = [(v, c) for c, v in l2]
ex2 = dict(ex2)
#print(ex2['valor'])

l3 = [[2,3,4],
     [7,9,10],
     [12,13,14]]
ex3 = [elemento for linhas in l3 for elemento in linhas if elemento % 2 == 0]
#print(ex3)

l4 = 'Julio Cesar Costa Silva'
qt_letras = 2
ex4 = '-'.join([l4[indice:indice + qt_letras] for indice in range(0, len(l4), qt_letras)])
#print(ex4)

l5 = ['julio', 'luiz', 'maria', 'joao', 'pedrin']
ex5 = [nome.title() for nome in l5]
print(ex5)
