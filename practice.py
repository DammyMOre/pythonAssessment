"""
import statistics

grades = [1,2,2,5,7,7,2,1,1,1,1,3,4,5,6,7,8,9,10]

print(statistics.mean(grades))
print(statistics.median(grades))
print(statistics.mode(grades))
print(sorted(grades))

#print("Average is: ", sum(grades)/len(grades))

"""
"""
#ex 3.4
for work in range(1,3,1):
	for ans in range(1,8,1):	
		print("@", end =" ")
	print()

"""
"""
#ex 3.7

print ("number", "square", "cube", end="  ")

import math

for number in range (0,6):
	print(number, number*number, number**3,)
"""
"""
#ex 3.8
smallest = 0
sum = 0
average = 0
product = 0


user_input = float(input("enter a number: "))
smallest_num = user_input
largest_num = user_input
for number in range (1,5):
	user_input = float(input("enter a number: "))

	sum+=user_input
	average = sum/user_input
	#product = number**2

	
	if user_input < smallest_num:
		smallest_num = user_input

	
	if user_input > largest_num:
		largest_num = user_input

	

print ("sum is: ", sum ,"average is: ", average, "product is: ", user_input**2)
print(smallest_num)
print(largest_num)

"""

array = []
sum = 0
for number in range(1,5):
	user_input = int(input("enter a number: "))
	sum+=user_input
array.append(sum)
	
#array.sort()
#print(sum)
print (array)


