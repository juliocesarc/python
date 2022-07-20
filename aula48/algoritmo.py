import re
from random import randint


REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj):
    cnpj = limpa_cnpj(cnpj)
    
    if eh_sequencia(cnpj):
        print('É uma sequencia!')
        return False

    try:
        novo_cnpj = calcula_digito(cnpj, 1)
        novo_cnpj = calcula_digito(novo_cnpj, 2)
    except Exception as e:
        print(e)
        return False

    return novo_cnpj


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None
    total = 0
    for indice, n in enumerate(regressivos):
        total += int(cnpj[indice]) * n

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'

def limpa_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if cnpj == sequencia:
        return True
    else:
        return False

def gera():
    numero = str(randint(10000000, 99999999))
    cnpj = f'{numero}000100'
    novo_cnpj = calcula_digito(cnpj, 1)
    novo_cnpj = calcula_digito(novo_cnpj, 2)
    return novo_cnpj

def formata():
    cnpj = gera()
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
