"""
	This module is the central program system. It is
	the the user interface of the system. Tkinter is the
	only GUI used here!
	No major functions are used here, all such functions are
	called from the other 3 modules.
"""

import tkinter as tk
import bank_jama as bj
import tkinter.messagebox
from random import randint
import user_database as ud
import jama_search as js

LARGE_FONT = ("verdana", 12)
auto_id = 000
cust = []
index = 0
#customer_identity = 0
class identity_User:
	def __init__(self, id):
		self.id = id

	def set_id(new_id):
		id = new_id

	def get_id():
		return id

var = []
class BigBossGui(tk.Tk):
	
	def __init__(self):
		tk.Tk.__init__(self)

		#Creating the container?

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=5)
		container.grid_columnconfigure(0, weight=9)

		""" 		Where the multiple windows will be stored """
		self.frame_container = {}

		for window in (Login, Login_Or_Register, MainMenu, CheckBalance, MakeDeposit, Withdraw, CreateAccount, ExitSystem):
			frame = window(container, self)

			self.frame_container[window] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.display_window(Login_Or_Register)

	def display_window(self, cont):
		frame = self.frame_container[cont]
		frame.tkraise()

class Login_Or_Register(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Welcome To Bank Jama")
		label.pack(pady=12, padx=12)

		# Login and Create Account.
		login_btn = tk.Button(self, text="Login",
												command=lambda:controller.display_window(Login))
		login_btn.pack()

		register_btn = tk.Button(self, text="Create Account",
												command=lambda:controller.display_window(CreateAccount))
		register_btn.pack()




class Login(tk.Frame):
	print("Login Form")
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Login")
		label.pack(pady=12, padx=12)
		self.parent = parent
		self.controller = controller

		self.username_label = tk.Label(self, text="Full Name:")
		self.username_label.pack(side="left")#grid(row=0)
		self.username = tk.Entry(self)
		self.username.pack(side="left")#grid(row=0, column=1)

		self.identity_label = tk.Label(self, text="ID:")
		self.identity_label.pack(side="left")#grid(row=0)
		self.identity = tk.Entry(self)
		self.identity.pack(side="left")#grid(row=0, column=1)
		
		self.submit = tk.Button(self, text="submit", command=lambda:self.go(self.parent, self.controller))
		self.submit.pack(side="right")

		self.back = tk.Button(self, text="Exit", command=lambda:controller.display_window(Login_Or_Register))
		self.back.pack(side="right")


	def go(self, parent, controller):
		# Check the users identity and name.
		print("Login Go")
		found_user = False
		for user in bj.users:
			if (str(self.username.get()) == user.full_name) and (int(self.identity.get()) == user.id) :
				# Detail inputted is correct.
				found_user =True
				bj.set_current_user(int(user.id))
				self.back_home = tk.Button(self, text="Enter Main Menu", 
											command=lambda:self.controller.display_window(MainMenu))
				self.back_home.pack(side="left")
				
		if found_user == False:
			tkinter.messagebox.showinfo('Window Title', "Incorrect User or Pin.")

class MainMenu(tk.Frame):
	""" The main menu where the user is presented when they log in correctly."""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
		label.pack(pady=12, padx=12)
		#check balance, deposit, withdraw, create account, exit.
		check_balance_btn = tk.Button(self, text="Check Balance", 
													command=lambda:controller.display_window(CheckBalance))
		check_balance_btn.pack()
		make_deposit_btn = tk.Button(self, text="Make A Deposit", 
													command=lambda:controller.display_window(MakeDeposit))
		make_deposit_btn.pack()
		withdraw_btn = tk.Button(self, text="Make A Withdrawal", 
													command=lambda:controller.display_window(Withdraw))
		withdraw_btn.pack()
		exit_sys_btn = tk.Button(self, text="Logout", 
													command=lambda:controller.display_window(ExitSystem))
def make_buttons(self, choice):
	"""This function creates the buttons for two functions."""
	print("Make Buttons" + str(auto_id))
	self.choice = choice
	if self.choice != 0:
		self.entry_label = tk.Label(self, text="Amount:")
		self.entry_label.pack(side="left")
		self.entry = tk.Entry(self)
		self.entry.pack(side="left")
			

	self.submit = tk.Button(self, text="submit", command=self.go)
	self.submit.pack(side="right")


class CheckBalance(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Check Balance", font=LARGE_FONT)
		label.pack(pady=12, padx=12)

		#MAKE CHOICE == 2
		self.choice = 0
		make_buttons(self, self.choice)

		self.back_home = tk.Button(self, text="Back to Home", 
											command=lambda:controller.display_window(MainMenu))
		self.back_home.pack(side="left")
	def go(self):
		# current user is gotten from function.
		current_User = bj.get_current_user()
		print(current_User)
		# user balance is returned from loop function from current user id.
		user_balance = bj.loop_through_users(int(current_User), int(self.choice), 0)
		message = "Your total Balance is €"+str(user_balance)
		tkinter.messagebox.showinfo('Window Title', message)


class MakeDeposit(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Deposit Cash", font=LARGE_FONT)
		label.pack(pady=12, padx=12)

		self.choice = 1
		make_buttons(self, self.choice)
		self.back_home = tk.Button(self, text="Back to Home", 
											command=lambda:controller.display_window(MainMenu))
		self.back_home.pack(side="left")
		
	def go(self):
		""" Deposit added to balance."""
		print("Deposit")
		# Get current user so as program knows who to give the cash too.
		current_User = bj.get_current_user()
		print(current_User)
		target = js.sort_through_ids(current_User, bj.users)
		if((float(self.entry.get()) > 2000) and self.choice ==  1):
			tkinter.messagebox.showinfo('Window Title', "Exceeds limits of deposit")
		else:
			# following function will append the users balance.
			bj.loop_through_users(int(current_User), int(self.choice), float(self.entry.get()))

class Withdraw(tk.Frame):
	print("Withdraw")
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Withdraw Cash", font=LARGE_FONT)
		label.pack(pady=12, padx=12)

		#MAKE CHOICE == 2
		self.choice = 2
		make_buttons(self, self.choice)

		self.back_home = tk.Button(self, text="Back to Home", 
											command=lambda:controller.display_window(MainMenu))
		self.back_home.pack(side="left")
	def go(self):
		print("User Withdrew")
		# current user gotten so as correct cash is given to correct user.
		current_User = bj.get_current_user()
		print(current_User)
		# user index number is found.
		target = js.sort_through_ids(current_User, bj.users)
		if((float(self.entry.get()) > bj.users[target].balance) and self.choice ==  2):
			tkinter.messagebox.showinfo('Window Title', "Insufficent funds")
		else:
			# following function will update the users balance.
			bj.loop_through_users(int(current_User), int(self.choice), float(self.entry.get()))

class CreateAccount(tk.Frame):
	print("Create Account")
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Create an Account", font=LARGE_FONT)
		label.pack(pady=12, padx=12)

		self.auto_id = auto_id
		self.username_label = tk.Label(self, text="Full Name:")
		self.username_label.pack(side="left")
		self.username = tk.Entry(self)
		self.username.pack(side="left")

		self.balance_label = tk.Label(self, text="Balance")
		self.balance_label.pack(side="left")
		self.balance = tk.Entry(self)
		self.balance.pack(side="left")

		self.submit = tk.Button(self, text="submit", command=self.go)
		self.submit.pack(side="right")

		self.back_home = tk.Button(self, text="Back to Home", 
												command=lambda:controller.display_window(Login_Or_Register))
		self.back_home.pack(side="left")

	def go(self):
		""" User is created """
		# random id for user is created between 0-1000
		random = randint(0,1000)
		# random is tested if it is unique, compared to the rest of user ids.
		test = bj.check_if_unique(random)
		while test == False:
			random = randint(0,1000)
			test = bj.check_if_unique(random)
		# if unique user is given the id random.
		self.auto_id = random
		user_id = "Your Personal Id is: "+str(self.auto_id)
		tkinter.messagebox.showinfo('Your ID, Remember this', user_id)
		# User is added into csv file and account.
		bj.create_account(int(self.auto_id), self.username.get(), float(self.balance.get()))
		# SYstem is restarted in order for user tobe shown.
		Begin_System()

class ExitSystem(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Goodbye!", font=LARGE_FONT)
		label.pack(pady=12, padx=12)
def Begin_System():
	""" In this function all user data will be created within the live system
		from csv file."""
	users = []
	users = ud.get_user_details()
	users = js.sort_by_id(users)
	bj.users = users
Begin_System()
app = BigBossGui()
app.title("Bank Jama")
app.minsize(width=400, height=400)
app.maxsize(width=800, height=800)

app.mainloop()

