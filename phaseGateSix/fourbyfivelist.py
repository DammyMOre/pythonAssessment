collect_row = int(input("enter row: "))
collect_colomn = int(input("enter colomn: "))


input = [[0]*collect_row ]*collect_colomn



for row in range(len(input)):
	for colomn in range (len(input[row])): 
		print (colomn*row , end = "  ")

	print()
