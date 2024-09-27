def odd_and_even_numbers(integer):
	for numbers in range(0,1000,1):

		if(numbers %2 == 0):
			return (numbers%2 + numbers %2)
		elif(numbers %3== 0):
			return (numbers %3 - numbers %3)

print(odd_and_even_numbers(22))


