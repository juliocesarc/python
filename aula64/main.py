from enum import Enum, auto

class Direcoes(Enum):
    direita = auto()
    esquerda = auto()
    cima = auto()
    baixo = auto()

def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('A direção inserida não está disponível!')
    return f'Movendo para {direcao.name}'

print(mover(Direcoes.direita))
print(mover(Direcoes.esquerda))
print(mover(Direcoes.cima))
print(mover(Direcoes.baixo))

for direc in Direcoes:
    print(direc.name)