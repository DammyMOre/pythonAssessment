add =0
count =0
average =0
for number in range(1,11,1):
	score = int(input("enter a score: "))
	if score>=0 and score <=100:
		count+=1
		add+=score
		average= add/count
print(average)
	