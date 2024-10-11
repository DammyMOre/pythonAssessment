"""
pseudo code
collect numbers between 1 and 50
for numbers divisible by 3, print fizz
for numbers divisible by 5, print buzz
for both, print fizzbuzz
"""

for numbers in range(1,51):
	if numbers%3 ==0 and numbers%5 ==0:
		print("fizzbuzz")
	elif numbers%3 ==0:
		print("fiz")
		continue
	if numbers%5 ==0:
		print("buzz")
		continue
	print(numbers)