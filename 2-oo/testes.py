from conta import Conta
from cliente import Cliente

conta_de_teste = Conta(1234, "Bruno", 55.6, 100.0)

print(conta_de_teste.saldo)

conta_de_teste.saca(200)
print(conta_de_teste.saldo)

print(conta_de_teste._Conta__pode_sacar(50))

print("=> Código do banco: {}".format(Conta.codigo_bancos()))

print("=> Taxa: {}".format(Conta.taxa))