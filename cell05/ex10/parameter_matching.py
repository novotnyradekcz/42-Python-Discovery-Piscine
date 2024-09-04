#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
	print("What was the parameter? ", end="")
	if input() == sys.argv[1]:
		print("Good job!")
	else:
		print("Nope, sorry...")
else:
	print("none")
