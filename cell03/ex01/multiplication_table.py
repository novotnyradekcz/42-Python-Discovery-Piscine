#!/usr/bin/env python3

number = None
while (number == None):
	print("Enter a number")
	try:
		number = int(input())
		for i in range(10):
			print(f"{i} x {number} = {i*number}")
	except ValueError:
		number = None
		print("Not a valid integer, try again, please")