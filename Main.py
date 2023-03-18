class Main:
	pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Pedro","29","Rua 8 de maio")
conta = Conta(100,"123581","pedro")

print("Nome: ", c1.nome,"\n", "Idade: ", c1.idade)

conta.depositar(-150)

print("Numero: ", conta.numero,"\n", "Saldo: ", conta.saldo)

print(dir(conta))