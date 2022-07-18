from vendas.calc_preco import aumento, reducao

def is_num(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except:
            print('Por favor digíte um numero válido, inteiro ou de ponto flutuante!')
            return 0

valor = is_num(input('Digite um número:  '))
p_centagem = is_num(input('Qual o aumento ou decremento que você quer aplicar?  '))
formatacao = bool(input('Caso devamos aplicar formatação digite qualquer coisa, caso contrario aperte "Enter"  '))

print(f'Com um aumento de {p_centagem}% resulta em: {aumento(valor, p_centagem, formatacao)}')
print(f'Com um decremento de {p_centagem}% resulta em: {reducao(valor, p_centagem, formatacao)}')
