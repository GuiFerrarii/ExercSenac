from historico import Historico
class Conta:
    def __init__(self,objeto,numero,saldo=0.0):
        self.titular = objeto.nome
        self.numero = numero
        self.saldo = saldo
        self.historico = Historico()

    def extrato(self):
        print(f'titular:{self.titular}'
              f'\nsaldo:{self.saldo}')
        self.historico.transacoes_bancarias()

    def saque(self,a):
        if a <= self.saldo:
            self.saldo = self.saldo-a
            self.historico.transacoes.append(f'saque de : {a}')
        else:
            print('saldo insuficiente')
    def recebe_transferencia(self, valor, conta):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo  += valor
            self.historico.transacoes.append(f'transferencias de: {valor} para {conta}')
        else:
            print('O saldo é insuficiente')
    def deposito(self,valor):
        self.saldo += valor
        self.historico.transacoes.append(f'deposito de : {valor}')

