from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

setlocale(LC_ALL, '') 
"""String vazia ele pega a linguagem padrão do computador do usuário,
 ou posso colocar 'pt_BR.utf-8' """

data = datetime.now()
formatacao = data.strftime('%A, %d de %B de %Y')
print(formatacao)

mes_atual = int(data.strftime('%m'))
print(f'Este mês tem {mdays[mes_atual]} dias')


indice_dia, indice_mes = monthrange(2022, 7)
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
print(dias[indice_dia + 1])

ultimos_dias_dos_meses = [monthrange(datetime.now().year, mes) for mes in range(1, 13)]
print(ultimos_dias_dos_meses)