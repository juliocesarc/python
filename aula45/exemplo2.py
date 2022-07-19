def modificar(funcao):
    def funcao_que_vai_substituir():
        print('#' * 15)
        funcao()
        print('#' * 15)
        return funcao
    return funcao_que_vai_substituir

@modificar
def meu_nome():
    for i in 'julio':
        print(i)

variavel = meu_nome()
variavel()