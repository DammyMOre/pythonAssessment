"""
pseudo code
generate 2 integers randomly
save the first as random_integer
save the second as random_value
prompt the user to enter the guess
save it as guess
add random_integer+random_value
save it as random
if random = guess 
print true 
if random != guess 
print false
"""

import random

random_integer = random.randint(1, 100)
print(random_integer)
	
random_value = random.randint(1, 10)
print(random_value)
	
guess = int(input("what is the guess: "))

random = random_integer + random_value
if random == guess:
	print("true")
else:
	print("false")