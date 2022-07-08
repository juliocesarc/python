lista = [
    ['P1', 15],
    ['P2', 8],
    ['P3', 13],
    ['P4', 6],
    ['P5', 9],
    ['P6', 5],
]

lista.sort(key=lambda item: item[1])
print(lista)
print(sorted(lista, key=lambda i: i[0]))

"""
def funcao(arg, arg2):
    return arg * arg2

a = funcao(2, 2)

        ^
são a mesma coisa 
        |||

a = lambda arg, arg2: arg * arg2
print(a(2, 2))
"""