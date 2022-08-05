import os
import shutil

caminho_original = '/Users/eriki/Documents/estudos/python/'
caminho_novo = '/Users/eriki/Documents/estudos/python/aula68/teste/'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'O caminho {caminho_novo} já existe e não pode ser criado!')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if 'exercitando' in file:
            shutil.copy(old_file_path, new_file_path)
            print('Arquivos copiados com sucesso!')