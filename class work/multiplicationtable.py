print()

print ("     Multiplication Table       ")

for count in range(1,10,1):
	print("  ",count, end="    ")
print()

for numbers in range(1, 10, 1):

	for table in range(1, 10, 1):

		print(table, " ", numbers*table)
	print ()