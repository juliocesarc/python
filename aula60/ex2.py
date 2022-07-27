class A:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self.__dict__[key] = value

a = A()
a.nome = 'Julio César'
print(a.nome)