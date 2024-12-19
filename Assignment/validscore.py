add =0
count = 0
while True:
	score = int(input("enter a score: "))
	if score>=0 and score <=100:
		count+=1
		add+=score
	if count==10: 	
		print(add)
		break