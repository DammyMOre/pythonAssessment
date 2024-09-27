
menu="""
1- Deposit
2- Withdrawal
3- Ballance
0- Quit
what will u like to do?
"""
ballance =0

while True:
	options= int(input(menu))
if options==1:
	deposit = int(input("how much will you like to deposit"))
	ballance += deposit
	print("your ballance is: ", ballance)
	

