from account import Account
from random import randint
users = []
auto_id = 000

def create_account(auto_id, username, cash):
	id_number = auto_id
	print("Your Id is: " + str(id_number))
	full_name = username.title()
	balance = float(cash)
	new_user = Account(id_number, full_name.title(), float(balance))
	print("Full Name: "+full_name.title())
	users.append(new_user)

def loop_through_users(identity, options, amount):
	user_found = False
	print("User ID is: "+str(identity))
	for user in users:
		if((user.id == int(identity))):
			user_found = True
			print("ID: "+str(user.id))
			print("User: "+user.full_name)
			if(options == 0):
				return float(user.get_balance())
			elif(options == 1):
				deposit_amount = amount
				print("User deposited: "+str(deposit_amount))
				user.deposit(float(deposit_amount))
			elif(options == 2):
				withdraw_amount = amount
				print("User Withdrew: "+str(withdraw_amount))
				user.withdraw(float(withdraw_amount))
	if(user_found == False):
		print("User Could not be found.")