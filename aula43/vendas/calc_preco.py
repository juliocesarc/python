from vendas.formata.preco import real as rl

def aumento(valor, porcentagem, formata = False):
    r = valor + (valor * (porcentagem / 100))
    if formata == True:
        return rl(r)
    else: 
        return r

def reducao(valor, porcentagem, formata = False):
    r = valor - (valor * (porcentagem / 100))
    if formata == True:
        return rl(r)
    else:
        return r