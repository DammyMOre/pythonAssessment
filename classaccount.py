balance = 0
while True:
	user_input = input("press 1 for deposit, 2 for withdrawer and 3 for balance: ")
	if user_input =='1':
		deposit = float(input("enter deposit amount: "))
		balance += deposit

	elif user_input =='2':
		withdrawal = float(input("enter withdrawal amount: "))
		if balance < withdrawal:
			print("insufficient fund")
		else:
			balance -= withdrawal
			print("your balance is: ", balance)

	elif user_input =='3':
		print("your balance is: ", balance)
		break



