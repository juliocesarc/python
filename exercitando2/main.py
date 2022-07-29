from banco import Banco
from cliente import Cliente
from contas import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Julio', 17)
cliente2 = Cliente('Bruno', 23)
cliente3 = Cliente('Maria', 34)

conta1 = ContaPoupanca(15353, 1111, 0)
conta2 = ContaCorrente(15354, 2222, 0)
conta3 = ContaCorrente(15355, 3333, 0)

cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)
cliente3.adicionar_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado!')

print('#'*15)

if banco.autenticar(cliente2):
    cliente2.conta.sacar(40)
else:
    print('Cliente não autenticado!')