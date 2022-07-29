from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente:
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def adicionar_conta(self, conta):
        self.conta = conta

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
        if valor > self.saldo
            self.saldo -= valor
            print(f'Saque realizado com sucesso!')
            self.informacoes()
            return
        else:
            print(f'Este valor é superior ao saldo retido em conta!')