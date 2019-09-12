# coding: utf-8
import re

cpf = input('Informe seu CPF')
hora = input('Informe a hora') 



pattern1 = '^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$'
pattern = '[0-23]{2}\:[0-59]{2}'

val_cpf = re.match(pattern1, cpf)
val_hora = re.match(pattern, hora)

if val_cpf != None:
print(val_cpf)
else:
print("CPF Inválido")

if val_hora != None:
print(val_hora)
else:
print("Hora Inválida")