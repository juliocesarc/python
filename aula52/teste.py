class Pessoa:
    sla = 123
    @property
    def nome(self):
        return 'Julio César'

p1 = Pessoa()
print(p1.nome)
print(p1.sla)