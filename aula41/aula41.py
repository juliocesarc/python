def is_num(value):
    try: 
        value = int(value)
        return value
    except ValueError as error:
        try:
            value = float(value)
            return value
        except:
            print(f'Erro: {value}')

#while True:

numero = is_num(input('Digite um numero:  '))

if numero is not None:
    print(numero * 5)
else:
    print('Digite um numero, qualquer outro caracter sera desconsiderado')