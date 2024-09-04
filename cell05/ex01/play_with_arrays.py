#!/usr/bin/env python3

my_array = [2, 8, 9, 48, 8, 22, -12, 2]
my_new_array = []
for num in my_array:
	my_new_array += [num + 2]

print("Original array: " + str(my_array))
print("New array: " + str(my_new_array))