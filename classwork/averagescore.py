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

total = 0
count = 1
while score!=-1:
	score = float(input("enter score: "))
	total+=score
	count+=1
	average = total /count
print("average is: ", average)
