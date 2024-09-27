"""
collect number from user
keep collecting until the user is done
save as number
enter -1 to break
collect numbers in a list
"""

number =[]
average = 0
add =0
while True:
	numbers = int(input("enter numbers and 0 to stop: "))
	
	if numbers == 0: 	
		break
	number += [numbers]
	print(number)

for count in number:
	add += count 
	average = add/count
print(add)
print(average)
		