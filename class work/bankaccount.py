"""
prompt the user to enter a deposit
save it as deposit
prompt the user to enter withrawer
save it as withdrawer
count the number of deposit occurence
count the number of withdrawer occurence
account balance is deposit minus withdrawer
"""
page ="""
what will u like to do:
1. Deposit
2. withdrawal
3. Ballance
"""
print (page)
while options:=input(page):
	ballance = 0
	if options == 1:
		depositamount = float(input("enter amount to deposit"))
		amount = ballance + depositamount 
		print(" Your ballance is: ", amount )
	options =input(page)

	if options == 2:
		withdrawalamount = float(input("enter amount to withdraw"))
		amount = withdrawalamount - ballance
else:
	if (withdrawalamount > ballance):

		print("insufficient funds")

	options = input(page) 
	
	if options == 3:
	
		print("your ballance is: ", amount) 


"""
while deposit =


count = 0
count+1





while option1 =0


count =0
while count != 0
deposit = int(input("Enter deposit"))
	print("deposit",count)
	count +=1
	total deposit = deposit + count
  
withdraw = int(input("Enter withdraw"))
	print("withdraw",count)
	count+=1
total withdraw = withdraw + count

ballance = deposit - withdraw

print (ballance)"""