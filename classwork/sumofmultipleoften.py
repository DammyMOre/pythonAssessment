"""
for numbers in range(1,20_001,10):
	
	multiple = 20_000%10
	sum = numbers + multiple
	print(sum)
"""

sum=0
for numbers in range(1,20_001,10):
	sum+=numbers
print (sum)