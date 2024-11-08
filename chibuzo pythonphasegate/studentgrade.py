
number_of_students = int(input("enter number of students: "))
number_of_subjects = int(input("enter number of subjects: "))


save = """
	Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	Saved succesfully

	"""
print(save)

#heading = input("enter headings: ")
headings = []

while True: 
	heading = input("enter headings: ")
	headings.append(heading)
	print()
	if heading == "0":
		break
print("================================================================================================")
print(headings ,end = "    ")
print()
print("==================================================================================================")


"""
#subject = 
student_details = [[]*number_of_subjects]*number_of_students

for name_of_students in range (number_of_students):
	details = input("enter students name: ")

	for score_of_subjects in subject:
		student_score = input("enter score: ")

		print(student_details[name_of_students ],[student_score ])
print()



	#student_details.append(details)


	#for sub in range(number_of_subjects):
		#subject_info = input("enter subject name: ")
		#subject.append(subject_info)

"""		


std arr = []
name_of_std1 = input("enter students name: ")
score_of_std1 = int(input("enter score: 

#student_subjects = [number_of_subjects]
