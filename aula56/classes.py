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

    def falar(self):
        print('falar de Cliente')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomedaclass} está estudando...')

class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        super().falar()
        print(f'{self.nome} {self.sobrenome} está falando!')
