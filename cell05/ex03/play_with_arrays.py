#!/usr/bin/env python3

my_array = [2, 8, 9, 48, 8, 22, -12, 2]
my_new_array = []
for num in my_array:
	if num > 5:
		my_new_array += [num + 2]

print(my_array)
print(set(my_new_array))