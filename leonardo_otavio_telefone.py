# coding: utf-8

import re

telefone = input('Digite seu telefone: ')

pattern = re.compile(r"(\([0-9]{2}\)?\s)?([0-9]{4,5}\-?[0-9]{4})")

if pattern.match(telefone):
	print("telefone valido!")
else:
	print("telefone invalido!")