
for number in range(1,8):
	for numb in range(1,number,1):
		if numb%2==0: print("*", end=" ")
		elif numb%3==0: print("3", end=" ")
		elif numb%5==0: print("5", end=" ")
		else: print("1", end=" ")

	print()
	



for number in range(8,1,-1):
	for numb in range(1,number,1):
		if numb%2==0: print("*", end=" ")
		elif numb%3==0: print("3", end=" ")
		elif numb%5==0: print("5", end=" ")
		else: print("1", end=" ")

	print()
	
