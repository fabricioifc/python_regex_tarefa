# coding: utf-8

import re

telefone = input('Digite seu telefone: ')
cpf = input('Digite seu CPF: ')

pattern_telefone = '(\([0-9]{2}\)?\s)?([0-9]{4,5}\-?[0-9]{4})'
resultado = re.match(pattern_telefone, telefone)


if resultado != None:
	print("telefone valido!")
else:
	print("telefone invalido!")