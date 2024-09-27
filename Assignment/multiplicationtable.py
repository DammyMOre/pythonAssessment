"""
pseudo code

collect a number, 
save as input
multiply input by the number
save as multiply
print input * number= multiply
"""


input = int(input("enter a number: "))

for numbers in range(1,11,1):
	
	multiply = input *numbers
	print(input, "*", numbers, "=", multiply) 
