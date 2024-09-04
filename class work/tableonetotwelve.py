print()

print ("     Multiplication Table       ")

for count in range(1,10,1):
	print("  ",count, end="    ")
print()


for numbers in range(1, 13, 1):

	for table in range(1, 13, 1):

		print(numbers,"*",table,"=",numbers*table,"  ")

	print()
	print(end=" ")
