from account import Account
from random import randint
import math
#import string
users = []
auto_id = 000
user_identities = []
new_ids = []
def get_id_started():
	for n in users:
		new_ids.append(n.id)
def create_account(auto_id, username, cash):
	id_number = auto_id
	print("Your Id is: " + str(id_number))
	full_name = username.title()
	balance = float(cash)
	new_user = Account(id_number, full_name.title(), float(balance))
	print("Full Name: "+full_name.title())
	users.append(new_user)
	save_user_details_database(users[-1])

def get_user_details():
	""" When Program is run, user details are withdrawn from a csv file."""
	filename = 'userdata.csv'
	with open(filename, 'r') as f_obj:
		lines = f_obj.readlines()
		for line in lines:
			#print(line.split())
			take = line.split()
			gu_identity = int(take[0])
			gu_name = take[1].replace('_', ' ')
			gu_balance = float(take[2])
			new_user = Account(gu_identity, gu_name.title(), float(gu_balance))
			users.append(new_user)
			#run_through_users()


def run_through_users():
	for user in users:
		print(user.full_name +' '+ str(user.id) +' '+ str(user.balance))
		

def sort_through_ids(identity):
	""" Sort users by their Id's"""
	run_through_users()
	print("Begining to Sort")
	#print(user_identities[:])
	new_ids.sort()
	half = math.ceil(len(new_ids) / 2)
	"""print(half)
	print(new_ids[half])"""
	# Divide and Conquer.
	print(identity)
	print(new_ids[half])
	if new_ids[half] < identity:
		iterator = half
		while iterator < len(new_ids):
			if new_ids[iterator] == identity:
				print("Found Iterator at "+str(iterator))
				return iterator
			iterator +=1
	elif new_ids[half] > identity:
		iterator = half
		while iterator >= 0:
			if new_ids[iterator] == identity:
				print(iterator)
				return iterator
			iterator -=1
	else:
		print("Could Not find the number!")
		return -1

def sort_by_id():
	print("Begin Sort by Id Right NOW")
	users.sort(key=lambda x: x.id, reverse=False)
	#print(users)

def loop_through_users(identity, options, amount):
	print("Looping Through Users.")
	get_user_details()
	user_found = False
	print("Looking for personal Identity: "+str(identity))
	search_result = sort_through_ids(identity)
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
	else:
		print("Could Not Find the User!")

def get_names():
	""" Creating Fake Users. """
	filename = 'names.txt'
	with open(filename, 'r') as f_obj:
		lines = f_obj.readlines()

		for line in lines:
			#print(line.split())
			names_split = line.split()
			full_name = str(names_split[0] +' '+ names_split[1])
			balance = randint(0, 1000000)
			if len(user_identities) == 0:
				identity = randint(0,1000)
				user_identities.append(identity)
			else:
				random = randint(0,1000)
				test = check_if_unique(random)
				while test == False:
					random = randint(0,1000)
					test = check_if_unique(random)
				user_identities.append(random)
				identity = random
			create_account(int(identity), str(full_name), float(balance))
def check_if_unique(number):
	"""Check if the Id to be given is Unique or not. """
	# Mabye make the user_identities sorted and use
	# Divide and Conquer methodology.
	isUnique = True
	for num in user_identities:
		if num == number:
			isUnique= False
	return isUnique
def save_user_details_database(user):
	""" Implemented in the Create Account Use Case """
	filename = 'userdata.csv'
	with open(filename, 'a') as f_obj:
		name = user.full_name.replace(' ', '_')
		#name.
		balance = user.balance
		personal_id = user.id
		#user_detail = []
		user_detail = str(personal_id)+' '+ name + ' '+str(balance)+'\n'
		f_obj.write(user_detail)
		f_obj.close()
#get_names()
