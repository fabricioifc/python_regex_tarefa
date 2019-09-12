

import re


nome = input("Digite seu nome: ")

telefone = input("Digite seu telefone ( xx xxxxx-xxxx): ")

email = input("Digite seu email: ")



pattern_nome = '[A-Z]'

pattern_tel = '([0-9]{2}\s[0-9]{4,5}\-?[0-9]{4})'

pattern_email = '^\w*(\.\w*)?@\w*\.[a-z]+(\.[a-z]+)?$'


resultado_nome = None
resultado_tel= None
resultado_email = None

while (resultado_nome==None):
	
	resultado_nome = re.match(pattern_nome,nome) #procura resultado exato

	if (resultado_nome != None):
		break
		
	else:
		nome = input("Digite seu nome com as letras iniciais maiúsculas: ")


while (resultado_tel==None):
	
	resultado_tel = re.match(pattern_tel,telefone) #procura resultado exato

	if (resultado_tel != None):
		break
		
	else:
		telefone = input("Telefone invalido digite seu telefone com ddd novamente: ")

while (resultado_email==None):
	
	resultado_email = re.match(pattern_email,email)

	if (resultado_email != None):
		break
	
	else:
		email = input("Email invalido !! digite seu email novamente: ")


print("Nome: ",nome, "\nTelefone: ", resultado_tel.group(),"\nEmail:", resultado_email.group())






