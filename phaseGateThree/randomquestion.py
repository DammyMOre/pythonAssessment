import random

answer = 0
correct = 0
wrong = 0
for times in range(1,4,1):
	random_number1 = random.randint(1,10)	

	random_number2 = random.randint(1,10)

	print(random_number1)	
	print(random_number2)

	answer = int(input("Whats the difference between number 1 and number 2: "))

	correct_answer = random_number1 - random_number2

	if correct_answer < 0: 
		correct_answer = random_number2 - random_number1 

	if answer == correct_answer:
		correct = times - wrong
		print("correct")
	
	if answer != correct_answer:
		wrong = times - wrong
		print("you are wrong")
	
 

if correct > wrong:
	print("Your final score is: ", correct)

else:
	print("Your final score is: ", wrong)
