d1 = {'chave1':'valor da chave 1'}
d2 = dict(chave2 = 'valor da chave 2')

valor = d1['chave1']

if valor in d1.values():
    print('Este valor é válido!')
else:
    print('Este valor é inválido!')

clientes = {
    'cliente1':{
        'nome':'Julio',
        'sobrenome':'César'
    },
    'Cliente2':{
        'nome':'Ruanito',
        'sobrenome':'Pedrada'
    }
}

for n_cliente, d_cliente in clientes.items():
    print(n_cliente)
    for d_nome, d_sobrenome in d_cliente.items():
        print(f'\t{d_nome} = {d_sobrenome}')