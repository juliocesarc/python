class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_cliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1, 'Julio')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'Joaquina')
bd.inserir_cliente(4, 'Cirilo')
print(bd.__dados)
#bd.apagar_cliente(3)
#bd.listar_cliente()