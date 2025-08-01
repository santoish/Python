class Account:
	def __init__(self,ac_no,ac_name,ac_type,ac_pin):
		self.account_no = ac_no
		self.account_holder_name = ac_name
		self.account_type = ac_type
		self.account_pin = ac_pin
		self.account_balance = 0

	def display_account(self):
		print('\n\nACCOUNT INFORMATION')
		print('-------------------\n')
		print(f'Account No : {self.account_no}')
		print(f'Account Holder Name : {self.account_holder_name}')
		print(f'Account Typing : {self.account_type}')
		print(f'Account Balance : {self.account_balance}')

	def deposit(self,amount):
		try:
			self.account_balance += amount
			print(f'Rs.{amount} Deposited Successfully')
		except ValueError:
			print('Invalid Amount! Please Enter Numeric Value')

	def withdraw(self,amount):
		try:
			if amount <= 0:
				raise ValueError('Withdrawal Amount must be Positive')
			if amount > self.account_balance:
				raise ValueError ('Insufficient Balance')
			self.account_balance -= amount
			print(f'Rs.{amount} Withdrawed Successfully')

		except ValueError as e:
			print('Error : ',e)



	def check_balance(self):
		return self.account_balance

	def validate_pin(self,input_pin):
		return self.account_pin == input_pin



class Bank:
	def __init__(self):
		self.accounts = {}

	def add_account(self,account):
		self.accounts[account.account_no] = account
		print('Account Created Successfully\n')

	def get_account(self,account_number):
		return self.accounts.get(account_number)

	def delete_account(self,account_number):
		if account_number in self.accounts:
			del self.accounts[account_number]
			print('Account Deleted Successfully')
		else:
			print('Account not Found')

	def authenticate(self,account_number,account_pin):
		account = bank.get_account(account_number)
		if account and account.validate_pin(account_pin):
			return account
		else:
			print('Authentication Failed')
			return None



bank = Bank()

while True:
	print('---Welcome to BANK---')
	print('1.Create New Account')
	print('2.Access Existing Account')
	print('3.Exit')

	try:
		choice = int(input('Enter Choice (1-3) : '))
		if choice not in [1,2,3]:
			raise ValueError('Invalid Menu Option. Please Choose 1,2 or 3.')
	except ValueError as e:
		print('Input Error : ',e)
		continue

	if choice == 1:
		acc_num = input('Enter Account  Number : ')
		acc_name = input('Enter Account Holder Name : ')
		acc_type = input('Enter Account Type (Savings / Current) : ')
		acc_pin = input('Enter Account PIN : ')
		account = Account(acc_num,acc_name.capitalize(),acc_type.capitalize(),acc_pin)
		bank.add_account(account)

	elif choice == 2:
		acc_num = input('Enter Account Number : ')
		acc_pin = input('Enter Account Pin : ')
		account = bank.authenticate(acc_num,acc_pin)


		if account:
			while True:
				print('\n\n---Account Menu---\n')
				print('1.Deposit')
				print('2.Withdraw')
				print('3.Check Balance')
				print('4.View Account Details')
				print('5.Delete Account')
				print('6.Logout')

				try:
					option = int(input('Enter Option (1-6) : '))
					if option not in range(1,7):
						raise ValueError('Invalid Option. Choose Option between 1-6')
				except ValueError as e:
					print(e)
					continue

				if option == 1:
					try:
						dep_amount = int(input('Enter Amount to be Deposit : '))
						if dep_amount <=0 :
							raise ValueError('Amout must be greater than 0')
						account.deposit(dep_amount)

					except ValueError as e:
						print('Invalid Input',e)

				elif option == 2:
					try:
						withdraw_amount = int(input('Enter Amount to be Withdraw : '))
						if withdraw_amount <=0 :
							raise ValueError('Amount must be greater than 0')
						account.withdraw(withdraw_amount)

					except ValueError as e:
						print('Invalid Input',e)

				elif option == 3:
					print(f'Your Balance is : Rs.{account.check_balance()}')

				elif option == 4:
					account.display_account()

				elif option == 5:
					acc_num = input('Enter Account Number to be Delete : ')
					bank.delete_account(acc_num)
					break

				elif option == 6:
					break

				else:
					print('Invalid Option')

	elif choice == 3:
		print('Thank you for using Bank . Good Bye !')
		break

	else:
		print('Invalid Choice')

