# Operador ternário

idade = input('Qual sua idade ?')

if not idade.isnumeric:
    print('Por favor digitar um numero.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar'
    print(msg)