user_input = int(input("Enter a number: "))
reverse = 0
real_value = user_input
while user_input != 0:
	reverse = (reverse * 10) + user_input % 10
	user_input = user_input // 10

if reverse == real_value:
	print("Wow, it is a palindrome")

if reverse != real_value:
	print("Oops, it is not a palindrome")
