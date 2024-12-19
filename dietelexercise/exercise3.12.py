"""
pseudo code
collect an input from d user
reverse the number
if the reversed number is the same as the input collected, 
print, it is palindrome
if not,
print, it isnot a palindrome
"""

value = 0
reverse =value
#input = 0
user_input = int(input("enter a number: "))
while user_input != 0:
	value = (value*10) + user_input % 10
	user_input = user_input//10
print(value)

#if reverse == value: print("it is a pallindrome")
if reverse != value: print("it is not a pallindrome")