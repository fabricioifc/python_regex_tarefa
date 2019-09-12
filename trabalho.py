# coding: utf-8
import re

cpf = input('CPF do ciclano é: ')
pattern = '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$'

resultado = re.findall(pattern, cpf)


email = input('email: ')

pattern = '^\w*(\.\w*)?@\w*\.[a-z]+(\.[a-z]+)?$'
resultado2 = re.findall(pattern, email)

