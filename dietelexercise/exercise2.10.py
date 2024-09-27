number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
number3 = int(input("enter number3: "))
sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3

if (number1 < number2 and number1 < number3):
	smallest = number1

elif (number2 < number1 and number2 < number3 ):
	 smallest = number2
 
else: 
	smallest = number3
 
if (number1 > number2 and number1 > number3):
	largest = number1

elif (number2 > number1 and number2 > number3 ):
	 largest = number2
 
else: 
	largest = number3 



print("sum is", sum)
print("average is", average)
print("product is", product)
print("smallest is", smallest)
print("largest is:", largest) 

