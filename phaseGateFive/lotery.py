import random
#answer1 = 23
#answer2 = 10
#answer3 = 67


answer1 = int(input("enter your answer"))
answer2 = int(input("enter your answer"))
answer3 = int(input("enter your answer"))

guess1 = random.randint(10,100)
guess2 = random.randint(10,100)
guess3 = random.randint(10,100)
print(guess1,guess2,guess3)


if guess1 and guess2 and guess3 == answer1 and answer2 and answer3:
	print("wow, you won $5000 ")
elif guess1 or guess2 or guess3  == answer1 or answer2 or answer3:
	print("wow, you won $4000 ")
elif guess1 or guess2 or guess3 != answer1 or answer2 or answer3:
	print("oh, sorry, try again")