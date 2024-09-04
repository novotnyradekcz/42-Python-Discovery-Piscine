#!/usr/bin/env python3

number = None
while number == None:
	print("Give me a number: ", end="")
	try:
		number = float(input())
		if number == int(number):
			print("This number is an integer.")
		else:
			print("This number is a decimal.")
	except:
		print("Not a valid number, try again, please.")
		number = None