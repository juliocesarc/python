from itertools import zip_longest, count

nome = 'Julio'
sobrenome = 'Cesar C'
contador = count()

nome_sobren = zip_longest(nome, sobrenome)

for n in nome_sobren:
    print(n)