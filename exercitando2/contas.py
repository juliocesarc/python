from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, cont, ag, saldo):
        self.conta = cont
        self.agencia = ag
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def informacoes(self):
        print(f'Conta: {self.conta}\nAgencia:{self.agencia}\nSaldo: {self.saldo}$')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Este valor é superior ao saldo retido em conta!')
            return
        self.saldo -= valor
        self.informacoes()

class ContaCorrente(Conta):
    def __init__(self, conta, ag, saldo, limite=300):
        super().__init__(conta, ag, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.limite + self.saldo) < valor:
            print('Saldo insulficiente ou limite atingido!')
            return
        self.saldo -= valor
        self.informacoes()