from time import time
from time import sleep

"""
def master(funcao):
    def slave():
        print('Agora estou decorada!')
        funcao()
    return slave

@master
def fala_oi():
    print('Oi')

#fala_oi = master(fala_oi)
fala_oi()
"""

def velocidade(funcao):
    def interna():
        start_time = time()
        resultado = funcao()
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar!')
        return resultado
    return interna

@velocidade
def demora():               #demora = velocidade(demora)
    for i in range(5):      #demora = interna
        print(i)     
        sleep(1) 

demora()