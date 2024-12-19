number = 5
count = 0

if number>1:
	for num in range (5):
		if number % num == 0:
			count+= num
if count==2: print("it is prime number")
else: print("it is not a prime number")
