"""
pseudo code
collect principal from user
collect interest from user
collect the number of years of investment
divide the interest by 100 and save as interest rate
multiply the interest rate by principal
save as interest_amount
repeat the action for the number of years of investment
print result
"""  
years = 0
PERCENTAGE = 100
principal = float(input("enter principal: "))
interest = float(input("enter interest: "))
number_of_years = int(input("enter number of years: "))

print(" year\t interest_amount \t balance " )

for year in range(1,number_of_years+1):

	interest_amount = interest/100 * principal
	first_year = principal + interest_amount
	
	principal = first_year

	print(f"{year}\t {interest_amount:,.2f}\t\t\t{first_year:,.2f}")

