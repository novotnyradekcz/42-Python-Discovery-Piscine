#!/usr/bin/env python3

first = None
while (first == None):
	print("Enter the first number:")
	try:
		first = int(input())
	except:
		first = None
		print("Not a valid number, try again.")

second = None
while (second == None):
	print("Enter the second number:")
	try:
		second = int(input())
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
