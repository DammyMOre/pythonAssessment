"""
pseudo code
create 10 numbers randomly
count the length of the numbers
check for the elements at even positions
sum  all elements at even positions
save in a variable sum_even_poition
check for all elements at odd positions
sum them up and save in a variable sum_odd
multiply all elements at every third positions
sum all the elements together and save as total
divide total by the number of the element length
save as average
display result
"""
import random
sum_even_position = 0
sum_odd_position = 0
multiply_third_position = 1
total = 0
average = 0
positions = []
for positions in range(1,11,1):
	numbers = random.randint(1,50)
	print(numbers)

	if positions%2==0:
		sum_even_position += numbers

	if positions%2-1 ==0:
		sum_odd_position += numbers

	if positions%3 == 0:
		multiply_third_position *= numbers

	if positions%1 == 0:
		total += numbers
	average = total/positions


print("sum_even_position is: ", sum_even_position )
print("sum_odd_position is: ", sum_odd_position )
print("multiply_third_position is: ", multiply_third_position)
print("total: ", total)
print("average: ", average)




#for elements in range(1,11,1):
