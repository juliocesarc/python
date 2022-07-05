def func(*args, **kwargs):
    #print(args, kwargs)
    idade = kwargs.get('idade')

    if idade is None:
        print('Idade não foi definida')
    else:
        print(idade)

lista = [1, 2, 3, 4, 5]
func(*lista, nome = 'Julio', sobrenome = 'César', idade = '17')