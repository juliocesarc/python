# ex 01

"""
def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', 'João')
"""

# ex 02

"""
def soma(one, two, tree):
    print(one + two + tree)

soma(5, 3, 2)
"""

# ex 03

"""
def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(10, 10)
aumento_percentual(100, 10)
aumento_percentual(600, 10)
"""

# ex 04

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'Fizz Buzz - (3 e 5) {n}'
    elif n % 3 == 0:
        return f'Fizz - (3) {n}'
    elif n % 5 == 0:
        return f'Buzz - (5) {n}'
    return n 

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))