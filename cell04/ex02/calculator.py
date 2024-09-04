#!/usr/bin/env python3

first = None
while first == None:
	print("Give me the first number: ", end="")
	try:
		first = int(input())
	except:
		print("Not a valid number, try again, please.")
		first = None

second = None
while second == None:
	print("Give me the second number: ", end="")
	try:
		second = int(input())
	except:
		print("Not a valid number, try again, please.")
		second = None

print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
if second == 0:
	print(f"{first} / {second} = undefined")
else:
	print(f"{first} / {second} = {first / second}")
print(f"{first} * {second} = {first * second}")