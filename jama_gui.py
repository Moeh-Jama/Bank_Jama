import tkinter as tk
import bank_jama as bj
import tkinter.messagebox
from random import randint

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

		#__init__(self, parent, controller)
		found_user = False
		for user in bj.users:
			if (str(self.username.get()) != user.full_name) or (int(self.identity.get()) != user.id) :
				print(str(self.username.get())+" Is incorrect ["+str((int(self.identity.get()))) +":"+str(user.id)+"]")
			else:
				# Detail inputted is correct.
				found_user =True
				n = int(self.identity.get())
				print("Lenght of Var is: "+ str(len(var)))
				if len(var) == 0:
					print("empty var")
					result = n
					var.append(result)
				else:
					print("Full var")
					var.pop(0)
					result = n
					var.append(result)
				print("Lenght of Var is: "+ str(len(var)))
				#cust[index] = customer_identity
				print(var)
				print("CU I"+str(var))
				self.back_home = tk.Button(self, text="Back to Home", 
											command=lambda:self.controller.display_window(MainMenu))
				self.back_home.pack(side="left")
		if found_user == False:
			tkinter.messagebox.showinfo('Window Title', "Incorrect User or Pin.")




class MainMenu(tk.Frame):

	
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
	#MAKE CHOICE == 2
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
		
		if self.choice == 0:
			final = bj.loop_through_users(int(var[0]), int(self.choice), 0)
			message = "Your total Balance is €"+str(final)
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
		for user in bj.users:
			if ((float(self.entry.get()) <0) and self.choice ==  1):
				tkinter.messagebox.showinfo('Window Title', "Sorry Cannot do that.")
			else:
				bj.loop_through_users(int(var[0]), int(self.choice), float(self.entry.get()))

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
		for user in bj.users:
			if((float(self.entry.get()) > user.balance) and self.choice ==  2):
				tkinter.messagebox.showinfo('Window Title', "Insufficent funds")
			else:
				bj.loop_through_users(int(var[0]), int(self.choice), float(self.entry.get()))

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
		self.auto_id = randint(0,1000)
		bj.create_account(int(self.auto_id), self.username.get(), float(self.balance.get()))
		
#prime id_er

class ExitSystem(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Goodbye!", font=LARGE_FONT)
		label.pack(pady=12, padx=12)



app = BigBossGui()
app.mainloop()