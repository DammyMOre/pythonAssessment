def only_float(a,b):

	if (a, float) and (b, float):
		return 2	
	elif (a, float) and (b, int):
		return 1
	
result = only_float(12.2 , 5)
