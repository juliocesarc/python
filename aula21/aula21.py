# definindo funções com def

def nomeDaF(mensagem = 'olá', nome = 'Julio'):
    return f'{mensagem} {nome}'

variavel = nomeDaF(nome = 'Julio C.', mensagem = 'Opa')
print(variavel)

"""
Caso a função não estiver recebendo um retorno seu valor será NONE,
isso quer dizer que pode ser usado dentro do 'if', se não estiver recebendo um retorno,
será lida como falso 
"""