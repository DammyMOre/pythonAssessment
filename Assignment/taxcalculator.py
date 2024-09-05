for numbers in range( 1, 3, 1): 
	name = input("Enter your name: ")
	earnings = int(input("Enter earnings: "))
	if(earnings <= 30000):
		taxrate = 15/100 * earnings
		print (taxrate)
	if (earnings > 30000):
		taxrate = 20/100 * earnings;
		print (taxrate)
