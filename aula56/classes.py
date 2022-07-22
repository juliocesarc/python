class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomedaclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomedaclass} está falando!')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomedaclass} está coprando!')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomedaclass} está estudando...')