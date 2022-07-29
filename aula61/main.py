"""
class Arquivo:
    def __init__(self, nome, modo):
        print('Abrindo arquivo')
        self.arquivo = open(nome, modo)
    
    def __enter__(self):
        print('Retornando o arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando o arquivo')
        self.arquivo.close()
    
    pass

with Arquivo('arquivo.txt', 'w') as file:
    file.write('Oi...')
"""

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo o arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando o arquivo')
        arquivo.close()

with abrir('aula61/abc.txt', 'w') as file:
    file.write('Opa...')