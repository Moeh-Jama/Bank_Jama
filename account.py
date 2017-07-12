class Account():

	def __init__(self, id, full_name, balance):
		self.id = id
		self.full_name = full_name
		self.balance = balance

	def get_balance(self):
		print("Your Current Balance is: "+str(self.balance))
		return self.balance
	def withdraw(self, withdraw):
		self.balance -= withdraw

	def deposit(self, deposit):
		self.balance += deposit