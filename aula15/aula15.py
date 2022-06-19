"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
############################### Split #############################
string = 'O Brasil e o o o pais do futebol e tudo mais'
lista = string.split(' ')

palavra = ''
contagem = 0

for valor in lista:
    # print( f'A palavra "{valor}" apareceu {lista.count(valor)}x vezes.' )

    # .strip() revome espaços do início e fim de uma str

    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes e ({palavra}) sendo ({contagem}x) vezes. ')

############################# (FECHA) Split ###############################

########################### Join #################################

list_join = ['Como', 'tancar', 'o', 'bostil', '?']
string_join = ' '.join(list_join)
print(string_join)

########################### (FECHA) Join #################################

########################### Enumerate #################################

frase = 'Como tancar o bostil ?'
string_cortada = frase.split(' ')

for indice, valor in enumerate(string_cortada): #, a partir de qual numero deve começar
    print(indice, valor, string_cortada[indice])


lista_com_listas = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for indice, valor in lista_com_listas:
    print(indice, valor)
########################### (FECHA) Enumerate #################################

