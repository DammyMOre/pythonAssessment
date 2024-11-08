
menu="""
1- Deposit
2- Withdrawal
3- Ballance
0- Quit
what will u like to do?
"""
ballance =0
#while menu != 0: 
	if menu==1:
		deposit = input("how much will you like to deposit")
		ballance += deposit
print(ballance)


