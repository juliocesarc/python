variavel = ['Julio', 'Cesar', 'Costa']

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Nenhuma das palavras começa com J')