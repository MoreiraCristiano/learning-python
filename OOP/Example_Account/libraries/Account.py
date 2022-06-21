from decimal import Decimal


class Account:
	# Construtor
	def __init__(self, name, balance):
		if (balance < Decimal("0.00")):
			raise ValueError("Initial balance must be gt 00.00.")

		self.name = name
		self._balance = balance

	def deposit(self, amount):
		if (amount < Decimal("0.00")):
			raise ValueError("Amount must be positive.")

		self._balance += amount

	def withdraw(self, amount):
		if (amount > self._balance):
			raise ValueError("Amount must be lt to balance.")
		if (amount < Decimal("0.00")):
			raise ValueError("Amount must be positive.")

		self._balance -= amount

	@property
	def balance(self):
		return self._balance
	# def get_balance(self):
	# 	return self._balance

	@balance.setter
	def balance(self, balance):
		self._balance = balance
	# def set_balance(self, balance):
	# 	self._balance = balance

