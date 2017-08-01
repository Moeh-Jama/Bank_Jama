"""
	This module holds functions that will be manipulating
	the csv files, creating large numbers of fake users and 
	adding more user objects to the system.
"""

from account import Account
from random import randint
def save_user_details_database(user, ab, users):
	""" Implemented in the Create Account Use Case """
	print("Save User Details....")
	filename = 'userdata.csv'
	with open(filename, ab) as f_obj:
		if ab == 'a':
			# if ab equals a then we will be only appending the file
			print("Appending Database")
			name = user.full_name.replace(' ', '_')
			balance = user.balance
			personal_id = user.id
			email = user.email
			user_detail = str(personal_id)+' '+ name + ' '+str(balance)+' '+email+'\n'
			f_obj.write(user_detail)
		elif ab=='w':
			# if ab equals w then program will re-write all user objects into the filename.
			print("Recreating Database")
			for persons in users:
				#print(persons.full_name)
				personal_id = persons.id
				name = persons.full_name.replace(' ', '_')
				balance = persons.balance
				email = persons.email
				user_detail = str(personal_id)+' '+ name + ' '+str(balance)+' '+email+'\n'
				f_obj.write(user_detail)
		f_obj.close()
	print("Save User Details Completed !!!")


def get_names(users):
	""" Creating number of Fake Users for testing """
	import bank_jama as bj
	filename = 'names.txt'
	with open(filename, 'r') as f_obj:
		lines = f_obj.readlines()

		for line in lines:
			#print(line.split())
			names_split = line.split()
			full_name = str(names_split[0] +' '+ names_split[1])
			balance = randint(0, 1000000)
			if len(bj.user_identities) == 0:
				identity = randint(0,1000)
				bj.user_identities.append(identity)
			else:
				random = randint(0,1000)
				test = bj.check_if_unique(random)
				while test == False:
					random = randint(0,1000)
					test = bj.check_if_unique(random)
				bj.user_identities.append(random)
				identity = random
			bj.create_account(int(identity), str(full_name), float(balance))

def get_user_details():
	""" When Program is run, user details are withdrawn from a csv file."""
	filename = 'userdata.csv'
	users = []
	with open(filename, 'r') as f_obj:
		lines = f_obj.readlines()
		for line in lines:
			#print(line.split())
			take = line.split()
			gu_identity = int(take[0])
			gu_name = take[1].replace('_', ' ')
			gu_balance = float(take[2])
			gu_email = take[3]
			new_user = Account(gu_identity, gu_name.title(), float(gu_balance), gu_email)
			users.append(new_user)
	return users