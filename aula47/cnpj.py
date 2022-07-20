import re

while True:
    def valida(cnpj):
        cnpj_limpo = limpa_cnpj(cnpj)
        novo_cnpj = str(algoritimos(cnpj_limpo[:-2]))
        novo_cnpj = str(algoritimos(novo_cnpj))
        
        print(novo_cnpj)

        if novo_cnpj == cnpj_limpo:
            print('CNPJ Válido!')
        else:
            print('CNPJ Inválido!')
        

    def limpa_cnpj(cnpj):
        return re.sub(r'[^0-9]', '', cnpj)

    def algoritimos(cnpj):
        contador = len(cnpj) - 7
        soma = 0
        
        for i in range(len(cnpj)):

            soma += contador * int(cnpj[i])

            if contador < 3:
                contador += 8
            contador -= 1

        if (11 - (soma % 11)) > 9:
            cnpj += '0'
        else:
            cnpj +=  str(11 - (soma % 11))
            
        return cnpj

    cnpj = input('Digíte um Cnpj:  ')

    valida(cnpj)