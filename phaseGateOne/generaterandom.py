"""
pseudo code
generate 2 integers randomly
prompt the user to enter the sum
report true if answer is correct 
report false if wrong
"""

import random

random_integer = random.randint(1, 10)	
for random_integer in range(1,2):
	print(random_integer)

random_integer = random.randint(1, 10)	
print(random_integer)

add = int(input("what is the sum"))
if random_integer + random_integer == add:
	print("true")
else:
	 print("false")