"""
write a function called maximum, it takes in three input and return the largest
 """
def maximum (firstnumber, secondnumber, thirdnumber):
	largestnumber=0

	if firstnumber > secondnumber:
		 largestnumber = firstnumber

	if secondnumber>largestnumber: 
		largestnumber = secondnumber


	if thirdnumber >largestnumber:
		largestnumber = thirdnumber


	return largestnumber

print(maximum(10,50,20))

