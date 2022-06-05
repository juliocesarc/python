secreto = 'perfume'
digitadas = []

while True:
    letra = input('Qual a letra de sua escolha?')

    if len(letra) < 1:
        print('É necessário que você digíte um único caracter, tente novamente.')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print('parabéns, você acertou!')
    else:
        print('você errou.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')