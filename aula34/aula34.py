import time

def gera():
    for i in range(100):
        yield i
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)

def gera2():
    variavel = 'Valor 1'
    time.sleep(0.2)
    yield variavel
    variavel = 'Valor 2'
    time.sleep(0.2)
    yield variavel
    variavel = 'Valor 3'
    time.sleep(0.2)
    yield variavel

g2 = gera2()

for a in g2:
    print(a)
