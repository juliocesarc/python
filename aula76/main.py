from time import sleep
from threading import Thread


"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Olá Julio C.', 5)
t1.start()

for i in range(20):
    sleep(.5)
    print(i)
"""
"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('Olá Julio C.', 5))
t.start()

for i in range(20):
    sleep(.3)
    print(i)

"""

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('Olá Julio C.', 10))
t.start()

while t.is_alive():
    sleep(2)
    print('Esperando a Thread!')
print('A thread acabou!')