#!/usr/bin/env python3

print("Enter a number less than 25")
try:
	number = int(input())
	if (number <= 25):
		while (number <= 25):
			print(f"Inside the loop, my variable is {number}")
			number += 1
	else:
		print("Error")
except:
	print("Error")
