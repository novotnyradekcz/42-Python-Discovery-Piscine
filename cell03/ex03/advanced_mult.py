#!/usr/bin/env python3

i = 0
while (i <= 10):
	j = 0
	print(f"Table de {i}: ", end="")
	while (j <= 10):
		print(i*j, end="")
		if (j < 10):
			print(" ", end="")
		else:
			print()
		j += 1
	i += 1