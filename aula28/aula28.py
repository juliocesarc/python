perguntas = {
    'pergunta1' : {
        'pergunta':'Quanto é 2+2?',
        'respostas': {
            'a':'1',
            'b':'4',
            'c':'5'
        },
        'resposta certa':'b'
    },
     'pergunta2' : {
        'pergunta':'Quanto é 2*3?',
        'respostas': {
            'a':'6',
            'b':'2',
            'c':'3'
        },
        'resposta certa':'a'
    }
}

print()
respostas_corretas = 0
for question, elements in perguntas.items():
    print(f'{question}: {elements["pergunta"]}')
    print()
    print('Respostas:')
    for r_letra, r_num in elements['respostas'].items():
            print(f'\t[{r_letra}] : {r_num}')
    resposta_usuario = input('Qual a alternativa correta ?  ')
    print()
    if resposta_usuario == elements['resposta certa']:
        print('Parabéns você acertou !')
        respostas_corretas += 1
    else:
        print(f'Você errou! A alternativa correta é a letra {elements["resposta certa"]}')
    print()
print(f'Você acertou {respostas_corretas / len(perguntas) * 100}% !')