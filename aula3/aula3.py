
nome = 'Julio'
idade = 16
altura = 1.74
peso = 60.5
ano = 2021
ano_nascimento = ano - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} só nasceu em {ano_nascimento}.')