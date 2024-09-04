#!/usr/bin/env python3

import statistics

def famous_births(persons):
	sorted_persons = dict(sorted(persons.items(), key=lambda person: int(person[1]["date_of_birth"])))
	for key, value in sorted_persons.items():
		print(f"{value['name']} is a great scientist born in {value['date_of_birth']}")

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)