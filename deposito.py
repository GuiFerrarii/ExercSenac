class Conta:
    def __init__(self, titular: str, numero: str, saldo: float):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def extrato(self):
        print(f'numero:{self.numero}\nsaldo:{self.saldo}')

    def deposito(self, valor):
        valor = float(valor)
        self.saldo = float(self.saldo)
        self.saldo += valor





