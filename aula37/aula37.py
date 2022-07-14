from itertools import zip_longest

lista1 = [1, 20, 7, 35, 8, 9, 15, 10, 4, 6, 3]
lista2 = [22, 31, 16, 2, 8, 19, 21, 17, 6]

total = [l1 + l2 for l1, l2 in zip_longest(lista1, lista2, fillvalue=0)]
print(total)