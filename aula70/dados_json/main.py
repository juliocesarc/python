"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""

from dados import *
import json
import os


# Converteu um objeto python em uma string no formato JSON
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8]
armazena = json.dumps(lista)
print(type(armazena), armazena)
"""

# Converte uma string JSON em python
"""
dicionario = json.loads(clientes_json)
for chave, valor in dicionario.items():
    print(chave)
    print(valor)
"""

pasta = os.path.dirname(__file__)

# Criou um arquivo JSON dentro desta mesma pasta, 
# pegou um dicionario python converteu para JSON e
# escreveu neste novo arquivo .json
"""
with open(f'{pasta}\clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)
"""

with open(f'{pasta}\clientes.json', 'r') as file:
    dados = json.load(file)

for chave, valor in dados.items():
    print(chave)
    print(valor)
