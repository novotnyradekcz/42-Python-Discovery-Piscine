#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
	occurences = sys.argv[2].count(sys.argv[1])
	if occurences > 0:
		print(occurences)
	else:
		print("none")
else:
	print("none")
