"""
	This module holds exclusively functions that deal with sorting,
	and searching user datas' 
	Along with printing out details of users for testing purposes. 
"""
import math
def run_through_users(users):
	""" used only in testing, Prints out users and their details. """
	get_user_details()
	for user in users:
		print(user.full_name +' '+ str(user.id) +' '+ str(user.balance)+ ' '+user.email)
def divide_and_conquer(identity, max_id, target):
	""" use a recurisve method to get the target user """
	from bank_jama import users
	index = int(identity)
	print(users[index].id)
	if users[index].id > target:
		# if current index is greater than target then half index
		# and limit the scope to the end of current index.
		return divide_and_conquer(math.ceil(index/2), index, target)
	elif users[index].id < target:
		# if current index is less than target then go to halfway of
		# current index and max index.
		# i.e. index = 1 max = 10 then new current index will be 5.
		num = math.ceil((max_id - index)/2)
		return divide_and_conquer(math.ceil(index+num), max_id, target)
	elif users[index].id == target:
		# finally if all other cases have failed the critieria we can assume,
		# we found the target.
		print("User found!")
		return index

def sort_through_ids(identity, users):
	""" Sort users by their Id's"""
	print("sort through ids...")
	# target index will be assigned the index of the identity after being 
	# returned by the divide and conquer function.
	target_index = divide_and_conquer(math.ceil(len(users))/2, len(users), identity)
	print("sorting through ids completed !!!")
	return target_index

def sort_by_id(users):
	""" Sort users array by id."""
	print("Begin Sort by Id Right NOW")
	users.sort(key=lambda x: x.id, reverse=False)
	print("Sort completed.")
	return users
