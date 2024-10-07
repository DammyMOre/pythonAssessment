duty_charge = 0
cost = int(input("enter cost of a car: "))

if cost > 10_000_000: 
	duty_charge = 0.2* cost
if cost >= 5_000_000 and cost < 10_000_000:
	duty_charge = 0.15* cost
if cost >=2_500_000 and cost < 5_000_000:
	duty_charge = 0.10 * cost
if cost < 2_500_000:
	duty_charge = 0.05 * cost

print ("duty_charge is: ", duty_charge) 
	