from datetime import datetime
from logging import exception

date = datetime.today()
details = []
customers_name= input("Enter customers name: ")
print("Please enter a valid input")
cashiers_name = input("Enter cashier name: ")

total_cost = 0
while True:
	items_bought = input("What did the customer buy: ")
	quantity = int(input("How many pieces:"))
	price_of_comodity = float(input("How much per unit: "))

	total = price_of_comodity * quantity
	total_cost += total
	details.append((items_bought, quantity, price_of_comodity, total))
	question = (input("Add more items"))
	if question=="yes":
		continue
	elif question=="no":
		break

print("Please enter a valid input")

heading = '''
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312,HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343
'''
print(heading)
print(date)
print("Cashier: ", cashiers_name )
print("Customer's Name: ", customers_name )
print("=======================================================================")        
print(f"	           {"ITEM":<20} {"QTY":5} {"PRICE":<10} {"TOTAL(NGN)":<10}")
print("-----------------------------------------------------------------------")

for item in details:
	print(f"              {item[0]:<20} {item[1]:<5} {item[2]:<10} {item[3]:<10.2f}")



print("-----------------------------------------------------------------------------")

print()

PERCENTAGE = 100
discount = float(input("How much is the percentage_discount: "))
percentage_discount = discount/PERCENTAGE * total_cost
vat = 17.50/PERCENTAGE * total_cost


print("Sub Total: ",  total_cost)
print("VAT @ 17.50%: ",  vat)
print("Discount: ",  percentage_discount)


print("======================================================================")

bill_total = (total_cost - percentage_discount) + vat
print("Your Total Bill is: ", bill_total)

print("======================================================================")

print("THIS IS NOT A RECIEPT KINDLY PAY    ", bill_total  )


print("======================================================================")
print("Total Bill: ", bill_total)
while True:
	amount_collected = int(input("How much did the customer give you: "))
	print("Amount paid: ", amount_collected)

	if amount_collected < bill_total:
		print ("your money is not complete, your bill is:", bill_total)
		continue
	elif amount_collected >= bill_total:
		break
print("Balance: ", amount_collected - bill_total)

print("============================================================================")
print("           THANK YOU FOR YOUR PATRONAGE        ")

print("===============================================================================")


