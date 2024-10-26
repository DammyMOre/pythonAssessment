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


student_details = []

for students in range (number_of_students):
	details = input("enter students name: ")
	student_details.append(details)

print(student_details)

#student_subjects = [number_of_subjects]
