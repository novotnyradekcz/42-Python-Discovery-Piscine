#!/usr/bin/env python3

first = None
while first == None:
	try:
		first = int(input("Give me the first number: "))
	except:
		print("Not a valid number, try again, please.")
		first = None

second = None
while second == None:
	try:
		second = int(input("Give me the second number: "))
	except:
		print("Not a valid number, try again, please.")
		second = None

print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
if second == 0:
	print(f"{first} / {second} = undefined")
else:
	print(f"{first} / {second} = {first / second:.0f}")
print(f"{first} * {second} = {first * second}")