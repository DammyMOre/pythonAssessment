"""
collect numbers between 1000 and 3000
each digit in the number is divisible by 2
the numbers should be separated by a comma
"""


import random

numbers = [] 
numb = 0

numbers = [random.randint(1000,3000)]
if numbers%2==0:
	print(numbers)
"""
while numbers!= 0:

	#if numbers % 100 and numbers % 10 ==0:
		#numb = numbers
		numbs = numbers%2
		numbers = numbers//10
		print(numb)
		break
"""	