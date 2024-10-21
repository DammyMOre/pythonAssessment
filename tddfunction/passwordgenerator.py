import string
import random

def get_password ():
	lowercase = string.ascii_lowercase
	uppercase = string.ascii_uppercase
	numbers = string.digits
	punctuation = string.punctuation
	
	collection = []

	
	for count in range(4):
		lower_case_selection = random.choice(lowercase)
		upper_case_selection = random.choice(uppercase)
		numbers_case_selection = random.choice(numbers)
		punctuation_case_selection = random.choice(punctuation)

	
		collection.append(lower_case_selection)
		collection.append(upper_case_selection)
		collection.append(numbers_case_selection)
		collection.append(punctuation_case_selection)
	

	return ''.join(collection)



print(get_password())