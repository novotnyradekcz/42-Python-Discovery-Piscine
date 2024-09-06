#!/usr/bin/env python3

import math

number = None
while number == None:
	try:
		number = float(input("Give me a number: "))
		print(math.ceil(number))
	except ValueError:
		print("Not a valid number, try again, please.")
		number = None