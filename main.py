from aula10 import Cliente
from Conta import Conta

cliente1 = Cliente(f'Guilherme Ferrari',
                   f'12345678-8','24/12/2002')

Conta1 = Conta(cliente1,123-4,100)

cliente2 = Cliente(f'Ferrari',
                   f'123123123-1','25/12/1998')

Conta2 = Conta(cliente2,134-6,500)



cliente1.imprime_dados()

Conta1.deposito(150)
Conta1.saque(50)

Conta2.extrato()
Conta1.saque(50)
Conta1.deposito(100)
Conta2.recebe_transferencia(10,Conta1)
Conta1.extrato()
Conta2.extrato()




