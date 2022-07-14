from itertools import groupby, tee

alunos = [
    {'aluno': 'Ko', 'nota': 'B'},
    {'aluno': 'Julio', 'nota': 'A'},
    {'aluno': 'Giovanna', 'nota': 'C'},
    {'aluno': 'Luana', 'nota': 'A'},
    {'aluno': 'Cleiton', 'nota': 'B'},
    {'aluno': 'Joana', 'nota': 'C'},
    {'aluno': 'João', 'nota': 'B'},
    {'aluno': 'Maria', 'nota': 'B'},
    {'aluno': 'Eduardo', 'nota': 'A'},
    {'aluno': 'André', 'nota': 'C'},
    {'aluno': 'Anderson', 'nota': 'A'},
    {'aluno': 'José', 'nota': 'A'},
    {'aluno': 'Fabricio', 'nota': 'C'},
]


ordena = lambda item: item['nota']

# modifica a lista, tornando-a organizada em ordem alfabética
alunos.sort(key = ordena)
# seleciona a lista já organizada, e roda a função a partir do valor de nota
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'agrupamento: {agrupamento}')

    for alunos in va1:
        print(alunos)

    quantidade = len(list(va1))
    print(f'{quantidade} de alunos tiraram nota {agrupamento}')



"""
func = lambda n: len(n['aluno'])

alunos.sort(key = func)

for i in alunos:
    print(i)
"""

