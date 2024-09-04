#!/usr/bin/env python3

import sys

try:
	if len(sys.argv) == 3:
		if int(sys.argv[1]) < int(sys.argv[2]):
			my_array = [x for x in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]
		else:
			my_array = [x for x in range(int(sys.argv[1]), int(sys.argv[2]) - 1, -1)]
		print(my_array)
	else:
		print("none")
except:
	print(f"Sorry, the parameters \"{sys.argv[1]}\" and \"{sys.argv[2]}\" are not valid integers.")
