
user_input = int(input("enter a number"))
reverse = 0
pallindrome = user_input
while user_input != 0:
	reverse = (reverse*10) + user_input % 10 
	user_input = user_input//10
print(reverse)