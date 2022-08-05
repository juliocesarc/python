class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index=None):
        """Envia como retorno o item alocado no índice enviado"""
        return self.__items[index]

    def __setitem__(self, index, valor):
        """Atribui um valor ou modifica de determinado indice enviado"""
        if index >= len(self.__items):
            self.__items.append(valor)
            return
        self.__items[index] = valor

    def __delitem__(self, indice):
        """Recebe um indice como parâmetro e o deleta"""
        if indice >= len(self.__items):
            print('Indice inexistente')
            return
        del self.__items[indice]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        """Modifica o retorno que seria o local da memória para uma string"""
        return f'{self.__class__.__name__}({self.__items})'

lista = MinhaLista()
lista.add('Julio')
lista.add('Cleber')
lista.add('Cleiton')
print(lista[2])
lista[3] = 'funciona?'
del lista[3]
print(lista)
