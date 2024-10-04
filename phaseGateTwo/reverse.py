"""
pseudo code
create a function
collect an integer from the user
reverse the number
if the number is a pallindrome,
return true
if it is not a pallindrome
return, it is not a pallindrome
"""

number = 0
def reverse(number):
	input = int(input("enter a number:"))
	number = (input * 10) + input % 10
	input = input // 10
	return (number)
