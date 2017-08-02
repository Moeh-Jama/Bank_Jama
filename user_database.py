"""
	This module holds functions that will be manipulating
	the database file customer_details, creating large numbers of fake users and 
	adding more user objects to the system.
"""

from account import Account
from random import randint
import sqlite3

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

conn = sqlite3.connect('customer_details.db')
c = conn.cursor()	# c is our cursor.

def create_table():									# unix time stamp.
	c.execute('CREATE TABLE IF NOT EXISTS customers(id REAL, full_name TEXT, balance REAL, email TEXT)')	# the cursor does all the execution of things...


def get_user_details():
	""" When Program is run, user details are withdrawn from a db."""
	print("Getting user details...")
	cursor = conn.execute("SELECT id, full_name, balance, email from customers")
	users = []
	for customer in cursor:
		customer_identity = int(customer[0])
		customer_full_name = str(customer[1])
		customer_balance = float(customer[2])
		customer_email = str(customer[3])
		new_user = Account(customer_identity, customer_full_name, customer_balance, customer_email)
		users.append(new_user)
	print("User details gathered....")
	return users

def customer_enter_database(new_user, users):
	""" In this function users are added to the customer_details database. """
	c.execute("INSERT INTO customers VALUES("+str(new_user.id)+", '"+str(new_user.full_name)+"', "+str(new_user.balance)+", '"+str(new_user.email)+"')")
	conn.commit()

def update_customer_balance(user, amount):
	""" Customers balance change is recorded into the database. """
	c.execute("UPDATE customers SET balance= ? WHERE id = ?", (user.balance, user.id))
	conn.commit()

#create_table()
