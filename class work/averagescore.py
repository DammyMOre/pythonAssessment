"""
pseudo code
collect score of students
save as score
initialize total to zero
initialize count to 1
while score is equal to -1
keep collecting score
add total to score
save as total score
when completely collected,
divide total score by number of students
save as average
display average

"""
score = 0
total = 0
count = 0

while score!=-1:
	score = float(input("enter score or -1 to quit: "))
	total+=score
	count+=1
	if(count!= 0):
		average = total /count
print("average is: ", average)
