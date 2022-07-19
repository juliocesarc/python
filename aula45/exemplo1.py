def decorador1(sua_funcao, *args, **kwargs):
    print('O decorador1 foi executado', end='\r\n\r\n')
 
    def funcao_que_vai_substituir_a_sua(*args, **kwargs):
        # só pra salpicar algo nos args (só funciona com strings e só nos args)
        print('Adicionando decorador1 nos args')
        manipulando_args = [f'{v} - decorador1' for v in args]
        return sua_funcao(*manipulando_args, **kwargs)
    return funcao_que_vai_substituir_a_sua
 
 
def decorador2(sua_funcao, *args, **kwargs):
    print('O decorador2 foi executado', end='\r\n\r\n')
 
    def funcao_que_vai_substituir_a_sua(*args, **kwargs):
        # só pra salpicar algo nos args (só funciona com strings e só nos args)
        print('Adicionando decorador2 nos args')
        manipulando_args = [f'{v} - decorador2' for v in args]
        print('Args agora:', *manipulando_args)
        return sua_funcao(*manipulando_args, **kwargs)
    return funcao_que_vai_substituir_a_sua
 
 
@decorador2  # decorador2 segundo
@decorador1  # decorador1 primeiro
def a_minha_funcao_1(msg):
    return msg
 
 
@decorador1  # decorador1 segundo
@decorador2  # decorador2 primeiro
def a_minha_funcao_2(msg):
    return msg
 
 
if __name__ == '__main__':
    print('RESULTADO COM a_minha_funcao_1:', a_minha_funcao_1('oi'))
    print()
    print('RESULTADO COM a_minha_funcao_2:', a_minha_funcao_2('Hello'))
 