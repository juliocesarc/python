cpf = '16899535009'
novo_cpf = cpf[:-2]
total = 0

reverso = 10

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if novo_cpf == cpf:
    print('CPF Valido!')
else:
    print('CPF Invalido')
