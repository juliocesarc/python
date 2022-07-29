"""
Faça um programa que leia duas notas de um aluno numa turma de 10 alunos. Para cada aluno, 
calcular a média ponderadas das notas, sabendo que a nota1 tem peso = 4 e a nota2 tem peso = 6.
 Imprimir a média do aluno e o conceito final, conforme tabela abaixo:

Intervalo     Conceito

0.0 a 4.9            D
5.0 a 6.9            C
7.0 a 8.9            B
9.0 a 10.0           A
Fazer 2 funções:

Função lambda para calcular a media ponderada das notas. Argumentos de entrada duas notas, Saída
 a média.
Função Local que irá receber como argumento de entrada a média das notas e retornar o conceito 
conforme a tabela acima.
"""

ponder = lambda n1, n2: n1 * 0.4 + n2 * 0.6

def conceito(media):
    if media < 5.0:
        m = 'D'
    elif media < 7.0:
        m = 'C'
    elif media < 9.0:
        m = 'B'
    else:
        m = 'A'
    return m
    
for i in range(10):
   nota1 = float(input('Digite a primeira Nota:'))
   nota2 = float(input('Digite a segunda Nota:'))
   media = ponder(nota1,nota2)
   conc = conceito(media)
   print("A média do aluno é:{0:.2f}".format(media)) 
   print("O conceito do aluno é:", conc) 