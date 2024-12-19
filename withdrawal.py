"""

menu="""
1. Deposit
2. withdrawal
3. Balance
0. End:"""

user_input = input(menu)

def get_transaction(amount,user_input):
	balance = 0

	if user_input =='1':

		balance += deposit
		return (balance)
	elif user_input =='2':
		withdrawal = float(input("enter withdrawal amount: "))
		if balance < withdrawal:
			print("insufficient fund")
		else:
			balance -= withdrawal
			print("your balance is: ", balance)

	elif user_input =='3':
		print("your balance is: ", balance)
		
	get_transaction(5000,1):


def deposit(amount):
	balannce+=amount
	return balance
def withdrawal(amount):
	if amount<balance
		balance -= amount
		return balance
	else: 
	 	return "insufficient funds"

def main():
	balance = 0
	option = input("enter 1 to deposit and 2 to withdraw: ")		if option =='1'
		amount =float(float(:enter deosit amount'))
		balance 


"""