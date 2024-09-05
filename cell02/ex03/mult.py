#!/usr/bin/env python3

first = None
while (first == None):
	try:
		first = int(input("Enter the first number: "))
	except:
		first = None
		print("Not a valid number, try again.")

second = None
while (second == None):
	try:
		second = int(input("Enter the second number: "))
	except:
		second = None
		print("Not a valid number, try again.")

result = first * second

print(f"{first} x {second} = {result}")

if (result == 0):
	print("The result is positive and negative.")
elif (result < 0):
	print("The result is negative.")
else:
	print("The result is positive.")
