num = input('Digíte um número inteiro: ')
hora = input('Digíte o horário atual: ')
nome = len(input('Qual seu nome: '))

if num.isnumeric():
    num = int(num)
    hora = int(hora)
    if num % 2 == 0:
        print(f'Você digitou um número par: {num}')
    else:
        print(f'Você digitou um número impar: {num}')
    if hora <= 11:
        print('Bom dia')
    elif hora > 11 and hora < 17:
        print('Boa tarde')
    else:
        print('Boa noite')
else:
    print('Este número não é inteiro, ou não é um número.')

if nome <= 4:
    print('Seu nome é muito curto.')
elif nome > 4 and nome <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito longo.')