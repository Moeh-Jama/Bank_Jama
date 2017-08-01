class Account():

	def __init__(self, id, full_name, balance, email):
		self.id = id
		self.full_name = full_name
		self.balance = balance
		self.email = email

	def get_balance(self):
		print("Your Current Balance is: "+str(self.balance))
		return self.balance
	def get_Email(self):
		print("User email is: "+self.email)
		return self.email
	def withdraw(self, withdraw):
		print("User Balance Was: "+str(self.balance))
		self.balance = self.balance - withdraw
		print("User Balance is Now: "+str(self.balance))

	def deposit(self, deposit):
		print("User Balance Was: "+str(self.balance))
		self.balance += deposit
		print("User Balance is Now: "+str(self.balance))