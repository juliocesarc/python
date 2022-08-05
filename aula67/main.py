import os

caminho_procura = input('Digíte um caminho: ')
termo_de_procura = input('Digíte um termo: ')

"""
raiz - pasta que está sendo verificada no momento
diretorios - pastas que estão dentro da raiz
"""

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')

conta = 0
for raiz, diretorio, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_de_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print(f'Encontrei o arquivo: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho (bits): {tamanho}')
                print(f'Tamanho formatado: {formata_tamanho(tamanho)}')
            except PermissionError:
                print('Sem permissão para acessar este arquivo!')
            except FileNotFoundError:
                print('Arquivo não encontrado!')
            except Exception as e:
                print('Erro desconhecido:', e)
print()
print(f'{conta} arquivo(s) encontrado(s).')