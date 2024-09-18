add =0
average = 0
count = 0
for number in range(1,11,1):
	score = int(input("enter a score: "))
	if(score%2 ==0):
		add+=score
		count+=1
		average= add/count
	
print(f"sum is: {add} \n average is: {average}")