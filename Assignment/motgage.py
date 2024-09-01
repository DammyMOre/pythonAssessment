"""
PSEUDO CODE
prompt the user to enter amount to borrow
save it as principal amount

prompt the user to enter a rate
save it as yearly rate

prompt the user to enter duration of repayment in years
save it as duration in years

store % as PERCENTAGE
store the numbers of months in a year as MONTHSINAYEAR 
multiply duration in years by MONTHSINAYEAR
save it as duration in months
divide yearly rate by PERCENTAGE by MONTHSINAYEAR
Add 1 + rate in month ** duration in month multiplied by rate in month
save it as rate calculator
Add 1+ rate in month**duration in months -1
save it as division
divide rate calculation by division
save as calculation 
multiply principal amount by calculation
save it as monthly repayment
print monthly repayment
"""





principalamount = float(input("enter amount: "))
yearlyrate = int(input("enter rate: "))
durationinyears = int(input("enter yearly duration: "))

PERCENTAGE = 100
MONTHSINAYEAR = 12

durationinmonth = durationinyears *MONTHSINAYEAR 

rateinmonth= yearlyrate /PERCENTAGE/MONTHSINAYEAR 

ratecalculation = rateinmonth * ((1 + rateinmonth)**durationinmonth)

division = ((1 + rateinmonth)**durationinmonth)-1

calculation = ratecalculation / division

monthlyrepayment = principalamount  * calculation

print("monthlyrepayment is $",round (monthlyrepayment, 2))





"""
ratecalculation = ((rateinmonth (1 + rateinmonth))**durationinmonth)/ ((1 + rateinmonth)**durationinmonth)-1
"""
