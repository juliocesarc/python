import json

d1 = {
    'Pessoa 1':{
        'idade': 25,
        'nome': 'Julio'
    },
    'Pessoa 2':{
        'idade': 32,
        'nome': 'Carla'
    }
}

d1_json = json.dumps(d1, indent=True)


with open('aula44/arquivo.json', 'w+') as filjs:
    filjs.write(d1_json)