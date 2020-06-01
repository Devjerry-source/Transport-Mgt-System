#Transportation Management System

'''GOD'S MOTOR LTD
'''
from datetime import datetime, timedelta
from random import sample
from pprint import pprint
from string import digits
from time import sleep
from sys import exit

status, status1, flag, flag1= False, False, False, False
destination_and_bus, bus_and_seats, seats, container, sub_container = [], [], 12, {}, {}
last_digits ="".join(sample(digits, 5))
#This creates a List of all employed drivers
drivers = ["Oluwafemi", "Johnson", "Babjide Olaoluwa", "Michael", "Faith", "Isaac", "James"]
#List of owned Bus number
bus_number = ["AGE5554", "ABJ4472", "EGD4551", "HJI7783", "EFH1694", "UWQ4951", "FTY1222"]
#This is the available destinations
destination = ["Port Harcourt", "Benin city", "Abuja", "Calabar", "Jos", "Ekiti", "Lagos"]
#This assigns a Driver to a Bus number
bus_and_drivers = [i for i in zip(bus_number, drivers)]
#This creates a display of the Bus seat numbers and with a defauLt None, signifying seat not assigned
seating = [{num: None for num in range(seats)} for i in range(7)]

numbers = ("0803", "0703", "0903", "0806", "0706", "0813", "0810", "0814", "0816",  "0805", "0705", "0905", "0807", "0815", "0811", "0905", "0809", "0909", "0817", "0818", "0802", "0902", "0701", "0808", "0708", "0812")

#Admin details
sub_container["Password"] = "Jerryibk999120"
container["Admin"] = sub_container

print("God's Motor ltd".upper().center(60, "*"))

def homepage():
	'''This is the Homepage of the TMS which allowd user to Login or Create an Account.
	'''
	global user_input, status
	
	print("Choose from the Options below.",                "Press 1 - Login",
	           "Press 2 - Create Account",
	           "Press 3 - Exit", sep = "\n")
	print()
	
	while status == False:
		try:
			user_input = int(input("To proceed Choose from the Above: "))
			if user_input == 1:
				login_portal()
				status = True
			elif user_input == 2:
				create_account()
				login_portal()
				status = True
			elif user_input == 3:
				exit
				status = True
			else:
				raise ValueError
		except ValueError:
			print()
			
			print("Invalid input!")

def create_account():
	'''This allows Unregistered Staff to create Account
	'''
	global first_name, last_name, password, gmail
	print("--" * 30)
	print("create account".upper())
	
	first_name = input("First Name: ").title()
	while first_name.isalpha() == False:
		print()
		
		print("Invalid input!")
		print()
		
		first_name = input("First Name: ").title()
	last_name = input("Last Name: ").title()
	
	while last_name.isalpha() == False or len(last_name) < 3:
		print()
		
		print("Invalid input!")
		print()
		
		last_name = input("Last Name: ").title()
	gmail = input("Gmail Address: ").lower()
	
	while gmail.endswith("@gmail.com") == False or len(gmail) < len("@gmail.com"):
		print()
		
		print("Invalid input!")
		print()
		
		gmail = input("Gmail Address: ").lower()
	
	password = last_name[:3] + last_digits
	print(f"Your default Password is {password}.", "Keep Your password safe to prevent Unauthorised access.", sep = "\n\n")
	name = first_name + " " + last_name
	sub_container = {}
	
	sub_container["Password"] = password
	sub_container["Gmail Address"] = gmail
	#This populates the container with the Staff's Login details'
	container[name] = sub_container
	print()
	
	print("Saved Sucessfully.....","Your Login Details are provided Below............", sep = "\n")
	sleep(1)
	print()
	print(f"Staff Name: {name}",
	          f"Password: {password}",
	          f"Gmail Address: {gmail} ", sep = "\n")
	print()
	
	print("Redirecting you to the Login Portal in 3secs...... ...... ....... ....")
	sleep(3)

def login_portal():
	global staff_name, user_password, status
	
	print("--" * 30)
	
	staff_name = input("Staff Name: ").title()
	user_password = input("Password: ")
	#This extracts the names in the container
	ext_name = [item for item in container.keys()]
	
	if staff_name not in ext_name:
		print()
		
		print("Staff Name or Password not in Data base.")
		print()
		
		print("Redirecting back to homepage... .... ..... ")
		sleep(2)
		
		status = False
		print("--" * 30)
		homepage()
	elif staff_name in ext_name and user_password not in container[staff_name]["Password"]:
		print()
		
		print("Staff Name or Password not in Data base.")
		
		print("Redirecting back to homepage... .... ..... ")
		sleep(2)
		
		status = False
		print("--" * 30)
		homepage()
	
	sleep(1)	
	menu()

def menu():
	'''This provides the Key features of the TMS
	'''
	
	global user_input_1, status1, status
	
	print("--" * 30)
	
	print("Choose from the Options below",                 "Press 1 - Seat Researvation",
	          "Press 2 - Bus & Seats Chart",
	          "Press 3 - Menu",
	          "Press 4 - Refresh Transactions", sep = "\n")
	print()
	
	while status1 == False:
		try:
			user_input_1 = int(input("To Proceed Choose from the Above: "))
			if user_input_1 == 1:
				status = False
				status1 = False
				flag = False
				seat_researvation()
				status1 = True
			elif user_input_1 == 2:
				status = False
				status1 = False
				flag = False
				bus_chart()
				status1 = True
			elif user_input_1 == 3:
				print("--" * 30)
				status = False
				status1 = False
				flag = False
				homepage()
				status1 = True
			elif user_input_1 == 4:
				sleep(1)
				status = False
				stutus1 = False
				flag = False
				for i in seating:
					for j in i.keys():
						i[j] = None
				menu()
				status1 = True
			else:
				raise ValueError
		except ValueError:
			print()
			
			print("Invalid Input!")
	        
def seat_num_prompt():
	global seat_num, flag
	
	while flag is False:
		try:
			seat_num = int(input("Seat number: "))
			if seat_num in range(seats + 1):
				flag = True
			else:
				raise ValueError
		except ValueError:
			print()
			
			print("Invalid input!")

def prompt():
	global user_prompt, flag, status
	
	user_prompt = input("To return to Menu enter 'm': ").lower()
	while user_prompt != "m":
		print()
		print("Invalid input!")
		
		user_prompt = input("To return to Menu enter 'm': ").lower()
	if user_prompt == "m":
		status = False
		status1 = False
		flag = False
		menu()			
		
def seat_researvation():
	global destination, customer_name, state, next_kin, phone_num, status1, flag, seat_num, user_prompt
	
	print("--" * 30)	    
	
	print("Seat Researvation".upper())
	
	customer_name = input("Name: ").title()
	
	while customer_name.isnumeric() == True or len(customer_name) < 3:
		print()
		
		print("Invalid input!")
		print()
		
		customer_name = input("Name: ").title()
	
	state = input("Destination (State): ").title()
	while state not in destination:
		print()
		
		print("Invalid input!")
		print()
		
		state = input("Destination (State): ").title()
	#This generates a default value for list_num for iteration
	if state == destination[0]:
		list_num = 0
	elif state == destination[1]:
		list_num = 1
	elif state == destination[2]:
		list_num = 2
	elif state == destination[3]:
		list_num = 3
	elif state == destination[4]:
		list_num = 4
	elif state == destination[5]:
		list_num = 5
	elif state == destination[6]:
		list_num = 6
	else:
		pass
	
	seat_num_prompt()
	while seating[list_num][seat_num] is not None:
		print()
		print("processing.... .... .... ....")
		print()
		sleep(1)
		
		print("Seat {} already occupied.".format(seat_num))
		print()
		flag = False
		seat_num_prompt()
		
	if seating[list_num][seat_num] is None:
		print("processing... ........ ..... ......")
		sleep(1)
		pass
	
	phone_num = input("Phone number: ")
	
	while phone_num.startswith(numbers) == False or phone_num.isnumeric() == False or len(phone_num) != 11:
		print()
		
		print("Invalid input!")
		print()
		
		phone_num = input("Phone number: ")
	next_kin = input("Next of Kin: ")
	while next_kin.isnumeric() == True or len(next_kin) < 3:
		print()
		
		print("Inalid input!")
		print()
		
		next_kin = input("Next of Kin: ")
	
	kin_num = input("Next of Kin Phone number: ")
	
	while kin_num.startswith(numbers) == False or kin_num.isnumeric() == False or len(kin_num) != 11:
		print()
		
		print("Invalid input!")
		print()
		
		kin_num = input("Next of Kin Phone number: ")
	bus = bus_number[list_num]
	print()
	
	print("Note: Ensure Payment, before selecting Paid.", "Payment of is Non-Refundable", "To select Paid, Enter Yes or No to select Paid", sep = "\n")
	
	payment = input("Paid>>> ").title()
	
	while payment not in ("Yes", "No"):
		print()
		
		print("Invalid input!")
		print()
		
		payment = input("Paid>>> ").title()
		
	print()
	if payment == "Yes":
		print("Receipt".upper())
		
		current_date = datetime.today()
		#default 1 hour for departure
		departure = datetime.today() + timedelta(minutes = 60)
		output = "| Name: {0},""  Destination (State): {1},""  Bus number: {2},"" Amount: 3500,""  Seat number: Seat {3},"" Departure Time: {4} |".format(customer_name, state, bus,seat_num, departure.time())
		                  
		print(output)
		#this fills the seat number with the customer's name
		seating[list_num][seat_num] = customer_name
	if payment == "No":
		flag = False
		status1 = False
		menu()
		
	prompt()
                 
def bus_chart():
	'''This displays the Different Buses and their correponding seats.
	It also displays the seats occupied and Unoccupied
	'''
	
	global bus_and_seats, destination_and_bus
	
	print("--" * 30)
	
	bus_and_seats = [i for i in zip(bus_number, seating)]
	#Creating a display of Buses and their destinations
	b = [destination_and_bus.append(item)for item in zip(destination, bus_and_seats)]
	print()
	
	pprint(destination_and_bus)
	
	prompt()
	
homepage()