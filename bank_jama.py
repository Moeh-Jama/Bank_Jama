from account import Account
from random import randint
import math
import user_database as ud
import jama_search as js
users = []
user_identities = []
current_user =  [] 
def create_account(auto_id, username, cash):
	""" User is created and appended to users array and 
	added to csv file """
	id_number = auto_id
	print("Your Id is: " + str(id_number))
	full_name = username.title()
	balance = float(cash)
	e_split =username.split()
	email = e_split[0].title()+'-'+e_split[1].title()+'@moemail.com'
	new_user = Account(id_number, full_name.title(), float(balance), email)
	print("Full Name: "+full_name.title())
	users.append(new_user)
	ud.save_user_details_database(new_user, 'a', users)

def get_current_user():
	return current_user[-1]
def set_current_user(user):
	current_user.append(user)
def loop_through_users(identity, options, amount):
	""" This function is used to find the user, their choice of 
		program function (deposit, get balance or withdraw cash)
	"""
	print("Looping Through Users.")
	#get_user_details()
	user_found = False
	print("Looking for personal Identity: "+str(identity))
	search_result = js.sort_through_ids(identity, users)
	# If we found a user then continue with the operations.
	if search_result != (-1):
		print("User is found at index: "+ str(search_result))
		user_found = True
		user = users[search_result]
		if(options == 0):
			print('Balance Section')
			return float(user.get_balance())
		elif(options == 1):
			print('Deposit Section')
			deposit_amount = amount
			print("User deposited: "+str(deposit_amount))
			user.deposit(float(deposit_amount))
		elif(options == 2):
			print('Withdraw Section')
			withdraw_amount = amount
			print("User Withdrawing : "+str(withdraw_amount))
			user.withdraw(float(withdraw_amount))
	if user_found == False:
		print("Could Not Find the User!")
	ud.save_user_details_database(users,'w', users)


def check_if_unique(number):
	"""Check if the Id to be given is Unique or not. """
	isUnique = True
	for num in user_identities:
		if num == number:
			isUnique= False
	return isUnique



""" Creating temporary Users """
ud.get_names(users)
"""
users = ud.get_user_details()
print(users[0].full_name)
users = js.sort_by_id(users)
index = js.sort_through_ids(165, users)
print(users[index].full_name)
"""