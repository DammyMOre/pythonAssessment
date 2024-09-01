
menu = '''1. Phone book

2. Messages 

3. Chat

4. Call register

5. Tones

6. settings

7. Call divert

8. Games

9. Calculator

10. Reminders

11. Clock

12. Profiles

13. SIM services
'''

print(menu)

phone_menu = int(input("enter a number: "))

if phone_menu == 1:
	
	print ('''
	phone Book :

	1. Search
	2.Service Nos
	3. Add name
	4.Erase
	5.Edit
	6.Assign tone
	7.Send b'card
	8.Options:
	  1. Type of view
	  2. Memory Status
	
	9. "Speed dials"
	10. "Voice tags"

''')
phone_book = int(input("enter a number: "))
if phone_book == 1:
	print("search")
if phone_book == 2:
	print("Service Nos")

if phone_book == 3:
	print("Add name")

if phone_book == 4:
	print("Erase")

if phone_book == 5:
	print("Edit")

if phone_book == 6:
	print("Assign Tone")

if phone_book == 7:
	print("Send b'card")

if phone_book == 8:
	print("Options")

options = int(input("enter a number: "))

if options ==1:
	print("Type of view")
if options ==2:
	print("Memory Status")

if phone_book == 9:
	print("Speed dials")
if phone_book == 10:
	print("Voice tags")

if phone_menu == 2:
	
	print ("Messages") 

if phone_menu == 3:

	print ("Chat")

if phone_menu == 4:

	print ("Call register")

if phone_menu == 5:

	print("Tones")

if phone_menu == 6:

	print ("Settings")

if phone_menu == 7:

	print ("Call divert")

if phone_menu == 8:

	print ("Games")

if phone_menu == 9:

	print ("Calculator")

if phone_menu == 10:

	print ("Reminders")

if phone_menu == 11:

	print ("Clock")

if phone_menu == 12:

	print ("Profiles")

if phone_menu == 13:

	print ("SIM services")







