car_make = input('Enter your car make>>> ')

display_info = ('''
AVAILABLE COMMANDS

'start' to start engine
'stop' to stop engine
'help' to display available commands
'exit' to terminate program 
''')

print(f'''
Welcome to your {car_make} dashboard
************************************
{display_info}
''')

execute = True 
engine_on = False

onDrive = False
onPark = False
onReverse = False

while execute:
	command = input("Enter command>>> ")
	
	if engine_on:
		if command == "start":
			print("Engine is ALREADY ON")

		elif command == "stop":
			print("Engine is OFF")
			engine_on = False

		elif command == 'D':
			if onDrive:
				print("Car is already in DRIVE mode")
			else:
				print("Car is now in DRIVE mode")
				onDrive = True
				onPark = False
				onReverse = False

		elif command == 'R':
			if onReverse:
				print("Car is already in REVERSE mode")
			else:
				print("Car is now in REVERSE mode")
				onDrive = False
				onPark = False
				onReverse = True

		elif command == 'P':
			print("Cannot engage PARK, put car OFF first")

		elif command == 'help':
			print(driving_info)

		else:
			print("Invalid command, enter 'help' to display driving info ")
		
	elif not engine_on:
		if command == "start":
			print("Engine is ON")
			engine_on = True

			driving_info = ('''
DRIVING INFO
'D' to Drive
'P' to Park
'R' to Reverse
'help' to display driving info
'exit' to terminate program 
		''')
			print(driving_info)

		elif command == "stop":
			print("Engine is ALREADY OFF ")

		elif command == 'P':
			if onPark:
				print("Car is already in PARK mode")
			else:
				print("Car is now in PARK mode")
				onDrive = False
				onPark = True
				onReverse = False

		elif command == 'D' or command == 'R':
			print("Cannot engage while car is OFF")

		elif command == 'help':
			print(display_info)

		else:
			print("Invalid command, enter 'help' to display available commands")

	if command == 'exit':
		print("Program ended")
		execute = False

