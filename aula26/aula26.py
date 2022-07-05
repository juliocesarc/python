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