'''
pseudo code
create a menu list for the pizza type, number of slices and price per box
print out the menu list
collect the number of guest
collect the pizza type
if case sapa size
print number_of_guess /4
if case small money
print number_of_guess /6
if case bigboys
print number_of_guess /8
if case odogwu
print number_of_guess /12

'''




menu_list = """

pizza type     Number of Slices     price per box

Sapa size              4                  2000

Small money            6                  2400

Big boys               8                  3000

Odogwu                 12                 4200


"""
print(menu_list)



number_of_guest = int(input("Enter number of guest: "))

pizza_type = input("pizza type: ")

match pizza_type:

	case "sapasize":

		print("boxes to buy is: " ,number_of_guest /4)

		print("remaining slices of pizza is: ", 4 - number_of_guest)

		print("your money is: ", 2000)
 
	case "small_money":

		print("boxes to buy is: ",number_of_guest /6)

		print("remaining slices of pizza is: " ,6 - number_of_guest)

		print("your money is: ", 2400)

	case "big_boys":

		print("boxes to buy is: ", number_of_guest /8)

		print("remaining slices of pizza is: ",8 -number_of_guest)

		print("your money is: ", 3000)


	case "odogwu":

		boxestobuy = number_of_guest /12

		print("boxes to buy is: ", number_of_guest /12)

if (number_of_guest>12):

	print("remaining slices of pizza is: ",number_of_guest-12)

elif (number_of_guest<=12):

		print("remaining slices of pizza is: ",12 - number_of_guest)


		print ("your money is: ", 4200)

if (number_of_guest > 12):
	 	print ("#", boxestobuy *4200)
	

