class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Getter
    @property
    def nome(self):
        print('GETTER')
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        print('SETTER')
        self._nome = valor.title()

p1 = Pessoa('JOÃOZINHO', 32)
print(p1.nome)