#!/usr/bin/env python3

def array_of_names(names):
	capitalized_names = []
	for key, value in names.items():
		capitalized_names += [f"{key.capitalize()} {value.capitalize()}"]
	return capitalized_names

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))