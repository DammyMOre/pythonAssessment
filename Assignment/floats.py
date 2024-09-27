def only_floats(number, numbers):
	if(number and numbers == float):
		return 2
	else:
		return 0

result = only_floats(1.5 , 2.3)
print(result)