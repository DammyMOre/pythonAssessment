add =0
average =0
for number in range(1,11,1):
	score = int(input("enter a score: "))
	add+=score
	average = add/10
print(f"sum is: {add} \n average is: {average}")