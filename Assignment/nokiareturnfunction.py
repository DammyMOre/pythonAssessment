def go_to_phone_menu():

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
			9. Speed dials
			10. Voice tags
	 		0. go back to phone menus
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
	if phone_book==0:
		print (go_to_phone_menu())

"""
if phone_menu == 2:

	print ('''
	Messages:
	1. Write messages
	2. Inbox
	3. Outbox
	4. picture messages
	5. Templates
	6. Smileys
	7. Message settings
		1. Set 1
	  	   1. Message centre number
	  	   2. Messages sent as
	  	   3. Message validity
		2. Common
	  	   1. Delivery reports
	  	   2. Reply via same centre
	  	   3. Character support
	8. Info service
	9. Voice mailbox number
	10. Service command editor

	''')

	messages = int(input("enter a number: "))
	if messages == 1:
		print("Write message")
	if messages == 2:
		print("Inbox")
	if messages == 3:
		print("Outbox")
	if messages == 4:
		print("picture message")
	if messages == 5:
		print("Templates")
	if messages == 6:
		print("Smileys")
	if messages == 7:
		print("Message Settings")
		message_settings = int(input("enter a number: "))
		if message_settings == 1:
			print("Set 1")
			set1 = int(input("enter a number: "))
			if set1 == 1:
				print("Message centre number")
			if set1 == 2:
				print("Messages sent as")
			if set1 == 3:
				print("message validity")
		if message_settings == 2:
			print("Common")
			common = int(input("enter a number: "))
			if common == 1:
				print("Delivery reports")
			if common == 2:
				print("Reply via same centre")
			if common == 3:
				print("character support")

	if messages == 8:
		print("Info service")
	if messages == 9:
		print("Voice mailbox number")
	if messages == 10:
		print("Service command editor")


if phone_menu == 3:

	print ("Chat")

if phone_menu == 4:

	print ('''
	Call Register

	1. Missed calls
	2. Received calls
	3. Dialled numbers
	4. Erase recent call lists
	5. Show call duration
	   1. Last call duration
	   2. All calls'duration
	   3.Recieved calls duration
	   4. Dialled calls duration 
	   5. Clear timers
	6. Show call costs
	   1.Last call cost
	   2. All calls' cost
	   3. Clear counters
	7. Call Cost settings
	   1. Call cost limits
	   2. Show costs in
	8. Prepaid credit
	''')
	call_register = int(input("enter a number: "))
	if call_register == 1:
		print("Missed calls")
	if call_register == 2:
		print("recieved calls")
	if call_register == 3:
		print("Dialled numbers")
	if call_register == 4:
		print("Erase recent call lists")
	if call_register == 5:
		print("Show call duration")
		show_call_duration = int(input("Enter a number: "))
		if show_call_duration == 1:
			print("Last call duration")
		if show_call_duration == 2:
			print("All calls duration")
		if show_call_duration == 3:
			print("Recieved calls duration")
		if show_call_duration == 4:
			print("Dialled calls duration")
		if show_call_duration == 5:
			print("Clear timers")
	if call_register == 6:
		print("Show call cost")
		show_call_cost = int(input("Enter a number: "))
		if show_call_cost == 1:
			print("Last call cost")
		if show_call_cost == 2:
			print("All calls cost")
		if show_call_cost == 3:
			print("Clear counters")
	if call_register == 7:
		print("Call cost Settings")
		call_cost_settings= int(input("Enter a number: "))
		if call_cost_settings == 1:
			print("call cost limits")
		if call_cost_settings == 2:
			print("Show costs in")
	if call_register == 8:
		print("Prepaid credit")

if phone_menu == 5:
	print('''Tones

1.Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
''')
	tones = int(input("Enter a number: "))
	if tones ==1:
		print("Ringing Tones")
	if tones ==2:
		print("Ringing volume")
	if tones ==3:
		print("Incoming call alert")
	if tones ==4:
		print("Composer")
	if tones ==5:
		print("Message alert tone")
	if tones ==6:
		print("Keypad tones")
	if tones ==7:
		print("Warning and game tones")
	if tones ==8:
		print("Vibrating alert")
	if tones ==9:
		print("Screen saver")

if phone_menu == 6:

	print('''

Settings

1. Call settings 
	1. Automatic redial
	2. Speed dialing
	3. Call waiting options
	4. Own number sending
	5. Phone line in use
	6. Automatic answer
2. Phone settings 
	1. language 
	2. Cell info display
	3. welcome note 
	4. Network Selection
	5. Lights
	6. Confirm SIM service actions
3. Call settings
	1. PIN code request
	2. Call baring services
	3. Fixed dialing
	4. Closed user group
	5. Phone security
	6. Change access codes
4. Restore factory settings ''')

	settings = int(input("Enter a number: "))
	if settings == 1:
		print("Call settings")
		call_settings = int(input("Enter a number: "))
		if call_settings == 1:
			print("Automatic redial")
		if call_settings == 2:
			print("Speed dialing")
		if call_settings == 3:
			print("call waiting options")
		if call_settings == 4:
			print("Own number sending")
		if call_settings == 5:
			print("phone line in use")
		if call_settings == 6:
			print("Automatic answer")

	if settings == 2:
		print("Phone settings")

		phone_settings = int(input("Enter a number: "))
		if phone_settings == 1:
			print("language")
		if phone_settings == 2:
			print("Cell info display")
		if phone_settings == 3:
			print("welcome note")
		if phone_settings == 4:
			print("Network selection")
		if phone_settings == 5:
			print("Lights")
		if phone_settings == 6:
			print("Confirm SIM service actions")

	if settings == 3:
		print("Security settings")

		security_settings = int(input("Enter a number: "))
		if security_settings == 1:
			print("PIN code request")
		if security_settings == 2:
			print("Call baring services")
		if security_settings == 3:
			print("Fixed dialling")
		if security_settings == 4:
			print("Closed user group")
		if security_settings == 5:
			print("phone security")
		if security_settings == 6:
			print("Change access codes")

	if settings == 4:
		print("Restore factory settings")



if phone_menu == 7:
	print("Call diverts")

if phone_menu == 8:
	print("Games")

if phone_menu == 9:
	print("Calculator")

if phone_menu == 10:

	print("Reminder")

if phone_menu == 11:

	print('''
Clock
1. Alarm clock
2. Clock setting
3. Date setting
4. Stop watch
5. countdown timer
6. Auto update of date and time
''')
	clock = int(input("Enter a number"))
	if clock == 1:
		print("Alarm clock")
	if clock == 2:
		print("Clock Setting")
	if clock == 3:
		print("Date setting")
	if clock == 4:
		print("Stop watch")
	if clock == 5:
		print("countdown timer")
	if clock == 6:
		print("Auto update of date and time")	


if phone_menu == 12:
	print("Profiles")

if phone_menu == 13:
	print("SIM Services")
"""