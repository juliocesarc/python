from classes import Cliente

cliente1 = Cliente('Julio', 17)
cliente1.insere_endereco('Curitiba', 'Paraná')
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Ronnie', 60)
cliente2.insere_endereco('Austin', 'Texas')
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Mike', 23)
cliente3.insere_endereco('Blumenal', 'Santa Catarina')
cliente3.lista_enderecos()
print()