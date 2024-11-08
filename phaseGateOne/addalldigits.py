"""
pseudo code
collect an integer between 0 and 1000
save as digit
sum the digits 
print result
"""

user_input = int(input("Enter a number ranging from 0 to 1000: "))
if user_input < 0 or user_input > 1000:
	print("Shout!!!")

sum_of_numbers = 0

while user_input != 0:
	sum_of_numbers += user_input % 10
	user_input = user_input // 10

print(sum_of_numbers)