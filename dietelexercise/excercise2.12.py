"""
pseudo code
store principal to be #1000
save one as 1
store rate to be 0.07
collect number of years from user
save as number of years
add 1 plus rate together and multiply by number of years
raise the result to the power of number of years
save the result as amount
display amount
"""

principal = 1000
one =1
rate = 0.07
number_of_years = int(input("enter number of years: "))
amount = (1+0.07)**number_of_years
expected_amount = amount*principal
print(round(expected_amount,2))