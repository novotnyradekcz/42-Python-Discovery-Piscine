#!/usr/bin/env python3

try:
	number = float(input())
	if (number == 0):
		print("This number is both positive and negative.")
	elif (number < 0):
		print("This number is negative.")
	else:
		print("This number is positive.")
except:
	print("This is not a valid number.")