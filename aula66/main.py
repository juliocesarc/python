from datetime import datetime, timedelta


dataJ = datetime.strptime('15/04/2005', '%d/%m/%Y')
data = datetime(2022, 7, 30, 11, 29)
temp = data - dataJ
print(f"Data formatada: {data.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Data timestamp: {data.timestamp()}")
print(f"Adicionando um intervalo de tempo: {data + timedelta(days=5)}")
print(f"Tempo de vida: {temp.days / 365}")