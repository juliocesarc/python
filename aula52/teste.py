class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return 'Julio César'

p1 = Pessoa()
print(p1.nome)
