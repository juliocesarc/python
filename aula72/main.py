from zipfile import ZipFile
import os

pasta_atual = os.path.dirname(__file__)
caminho = r'/Users/eriki/OneDrive/Nova pasta/'

# Copiando arquivos para dentro de uma pasta Zip
with ZipFile(f'{pasta_atual}/arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

# Lendo os arquivos de dentro da pasta compactada
with ZipFile(f'{pasta_atual}/arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile(f'{pasta_atual}/arquivo.zip', 'r') as zip:
    zip.extractall(f'{pasta_atual}/descompactado')
