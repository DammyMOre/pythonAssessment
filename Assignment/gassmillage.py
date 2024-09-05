trip = int(input("enter number of trips: "))
		
for numbers in range (1, trip, 1):
	miles= int(input("enter mile driven: "))

	totalmiles = miles + miles

	gallons = int(input("enter gallons:  "))

	totalgallons = gallons + gallons

	average = miles/gallons

	totalaverage = totalmiles/totalgallons

	print("Miles per Gallon is:" ,totalaverage)

