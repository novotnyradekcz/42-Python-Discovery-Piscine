#!/usr/bin/env python3

age = None
while age == None:
	print("Please tell me your age: ", end="")
	try:
		age = int(input())
		if age < 0:
			print("Not a valid age, try again, please.")
			age = None
		else:
			print(f"You are currently {age} years old.")
			for i in range(10, 40, 10):
				print(f"In {i} years, you'll be {age + i} years old.")
	except:
		print("Not a valid number, try again, please.")
		age = None