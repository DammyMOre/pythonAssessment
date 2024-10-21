"""
pseudo code
collect card number
the number should be between 13-16 digits
if the number starts with 4, 
display, it is visa card
if the number starts with 5,
dispay, it is master card
if the number start with 6,
display, it is discover cards
if the number start with 37,
display, it is American express cards
if the number did not start from any of the above, 
display, invalid card
check for numbers in the even index of each cards and multiply them
if the multiplication of the 2 digits results in 2 digit,
add it up to turn a single digit
add all the collected digits together,
save it as total_of_even 
add all digit in the odd index,
save it as total_of_odd
add total_of_even and total_of_odd together
save as total
if the result of total is divisible by 10
the card number is valid
if not, it is invalid
 
"""

card_number = input("enter your card number to verify: ")

card_length = len(card_number)
if card_length>=13 and card_length <= 16:

	if card_number.startswith("4"):
		print("credit card type is: visa card")
		print("creit card number is: ", card_number)
		print("credit card length is: ",card_length)

	elif card_number.startswith("5"):
		print("credit card type is: Master card")
		print("credit card number is: ", card_number)
		print("credit card length is: ",card_length)

	elif card_number.startswith("6"):
		print("credit card type is: Discover card")
		print("creit card number is: ", card_number)
		print("credit card length is: ",card_length)



	elif card_number.startswith("37"):
		print("credit card type is: American express card")
		print("credit card number is: ", card_number)
		print("credit card length is: ",card_length)


	else:
		print("invalid card")

else:
	print("invalid card")



























