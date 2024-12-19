#number_of_years = int(input("enter number of years: "))

year=0
for years in range(1,31):
	year+=years
	principal = 1000
	one =1
	rate = 0.07
	amount = (1+0.07)**years
	expected_amount = amount*principal
	print("expected amount"+"  ", "years")
	print(round(expected_amount,2),"           ", years)
