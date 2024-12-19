
import string
import random

def get_password ():

	lowercase = string.ascii_lowercase

	uppercase = string.ascii_uppercase

	numbers = string.digits

	punctuation = string.punctuation


	array = []

	for count in range (3):

		lower_case_collector = random.choice(lowercase)

		upper_case_collector = random.choice(uppercase)

		numbers_collector = random.choice(numbers)

		punctuation_collector = random.choice(punctuation)


		array.append(lower_case_collector)
		array.append(upper_case_collector)
		array.append(numbers_collector)
		array.append(punctuation_collector)


	return ''.join (array)

print(get_password())
