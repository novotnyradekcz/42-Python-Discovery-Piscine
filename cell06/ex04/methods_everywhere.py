#!/usr/bin/env python3

import sys

def shrink(string):
	return string[:8]

def enlarge(string):
	return string + "Z" * (8 - len(string))

if len(sys.argv) > 1:
	for arg in sys.argv[1:]:
		if len(arg) > 8:
			print(shrink(arg))
		else:
			print(enlarge(arg))
else:
	print("none")