import aula50

p1 = aula50.Pessoa('Julio', 17)
p1.get_ano_de_nascimento()
p2 = aula50.Pessoa.por_ano_de_nascimento('Luana', 1984)
print(p2.idade)
id = p2.gera_id()
print(id)
