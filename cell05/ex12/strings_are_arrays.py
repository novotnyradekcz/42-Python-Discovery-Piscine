#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
	occurences = sys.argv[1].count("z")
	if occurences > 0:
		print(occurences)
	else:
		print("none")
else:
	print("none")
