cpf = '16899535009'
cpf_lista = list(cpf)

print(cpf_lista)

contador = 10
novo_cpf = []
digito1 = 0

for indice_list in cpf_lista:
    if contador > 2:
        digito1 += contador * int(indice_list)
        print(digito1)

        contador -= 1
        
