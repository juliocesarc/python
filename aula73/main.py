from genericpath import isdir
import sys
import os

argumento = sys.argv
qtd_argumentos = len(argumento)

if qtd_argumentos == 1:
    print('Por favor digite algum argumento:')
    print('[pastas] para acessar aspastas deste mesmo arquivo')
    print('[arquivos] para acessar aspastas deste mesmo arquivo')
    sys.exit()

if qtd_argumentos != 1:

    if 'arquivos' in argumento:
        for arquivo in os.listdir('.'):
            if os.path.isfile(arquivo):
                print(arquivo)
    if 'pastas' in argumento:
        for diretorio in os.listdir('.'):
            if os.path.isdir(diretorio):
                print(diretorio)