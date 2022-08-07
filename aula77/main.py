from importlib import import_module
import PyPDF2
import os


caminho_da_pasta = os.path.dirname(__file__)
caminho_dos_pdfs = f'{caminho_da_pasta}\pdf'

"""
novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo = os.path.join(root, file)
        
        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""

with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wr') as novo_pdf:
            escritor.write(novo_pdf)