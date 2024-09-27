scores = [45,50,78,25,94,100]
scores[0] = 23
# meaning 45 will change to 23
print(scores[1])
print(len(scores))

additional_scores=[53, 32, 13]

scores+=additional_scores

#to add 10 to all scores

for index in range(len(scores)):
	scores[index]+=10
print (scores)

reverse_list=[]
'''
for index in range(len(scores)-1,-1,-1):
	reverse_list += [scores[index]]
'''
reverse_list=scores[::-1]

print(reverse_list)
