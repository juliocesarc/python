from abc import ABC, abstractclassmethod

class Conta(ABC):
    def __init__(self, conta, agencia, saldo):
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico!')
            return
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Depósito precisa ser numérico!')
            return
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print()
        print(f'Conta: {self._conta}')
        print(f'Agencia: {self._agencia}')
        print(f'Saldo atual: {self._saldo}')
        print()
        print('#' * 15)

    @abstractclassmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insulficiente!')
            return
        self._saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo, limite = 300):
        super().__init__(conta, agencia, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if self.limite < valor or self._saldo < valor:
            print('Não foi possível concluir está ação, saldo insulficiente ou limite excedido!')
            return
        print('Operação realizada com sucesso...')
        self._saldo -= valor
        self.detalhes()
