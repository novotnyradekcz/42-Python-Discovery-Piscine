#!/usr/bin/env python3

import math

number = None
while number == None:
	print("Give me a number: ", end="")
	try:
		number = float(input())
		print(math.ceil(number))
	except:
		print("Not a valid number, try again, please.")
		number = None