import json

with open('aula44/arquivo.json', 'r') as file:
    armazena = file.read()
    armazena = json.loads(armazena)

for c, v in armazena.items():
    print(c)
    for c2, v2 in v.items():
        print(c2, v2)
