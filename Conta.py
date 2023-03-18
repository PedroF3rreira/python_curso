class Conta:
	def __init__(self, saldo, numero, titular):

		self.__saldo = 0
		self.numero = numero
		self.titular = titular

	@property
	def saldo(self):
		return self.__saldo

	@saldo.setter
	def saldo(self, saldo):
		raise ValueError("use o método depositar para alterar valor do saldo")
		
	def depositar(self, saldo):
		if (saldo <= 0):
			print("o valor do saldo têm que ser positivo")
		else:
			self.__saldo = saldo