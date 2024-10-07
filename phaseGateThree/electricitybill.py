price =0
unit = int(input("enter your units: "))

if unit <= 100:
	print("No charge")
if unit > 100 and unit < 200:
	bal = unit - 100
	price = 50 * bal

	print("your price is: #", price)

if unit >= 200:
	balance = unit-100
	discount = balance *50
	available = unit-balance 
	price = 100 * available - discount
	print("your price is: #", price)


 