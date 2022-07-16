try:
    a = []
except TypeError as variavel_com_erro:
    print(f'Erro: {variavel_com_erro}')
except ZeroDivisionError as variavel_com_erro:
    print('Erro: divisão por zero pô')
except Exception as variavel_com_erro:
    print(f'Só um errin...')
else:
    print('Ocorreu tudo certinho, sem erro pae')
finally:
    a = [5, 4, 3, 2, 1]

print(a[1])
