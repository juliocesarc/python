""""
:s - texto(string)
:d - inteiro(int)
:f - float
:.(NUMERO) - quantidade de casas decimais float
:(caractere)(> ou < ou ^)(quantidade) (tipo s, d ou f)

> - esquerda
< - direita
^ - centro

"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')

print(f'{num_2:0>10}')
print(f'{num_2:0<10}')
print(f'{num_2:0^10}')