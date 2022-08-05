import csv


with open('aula69\clientes.csv', 'r') as file:
    dados = [x for x in csv.DictReader(file)]

with open('aula69\clientes2.csv', 'w+') as file:
    escreve = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #delimitados por vírgula, envolvidos por chaves duplas, atribui as aspas a todos os valores
    for dado in dados:
        escreve.writerow([dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone']])