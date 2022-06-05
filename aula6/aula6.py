"""
nome = input('Digite seu nome: ')
qtd_usuario = len(nome)

if qtd_usuario < 6:
    print('Seu nome contém menos de 6 caracteres.')
else:
    print('Seu nome possui 6 caracteres ou mais.')
"""

num_1 = input('Digíte um número: ')
num_2 = input('Digíte outro número: ')

if num_1.isnumeric() and num_2.isnumeric():
    print('É um número.')
    print(int(num_1) + int(num_2))
else:
    print('Algum dos valores não corresponde a um número.')
