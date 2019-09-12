

import re


nome = input("Digite seu nome: ")

telefone = input("digite seu telefone ( xx xxxxx-xxxx): ")

email = input("Digite seu email: ")






pattern_tel = '([0-9]{2}\s[0-9]{4,5}\-?[0-9]{4})'

pattern_email = '^\w*(\.\w*)?@\w*\.[a-z]+(\.[a-z]+)?$'


#resultado = re.search(pattern,telefone) # busca no texto o padrão
#resultado = re.findall(pattern,telefone) # busca 
resultado_tel=None
resultado_email = None

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




resultado_email = re.match(pattern_email,email)

print("Nome: ",nome, "\nTelefone: ", resultado_tel.group(),"\nEmail:", resultado_email.group())

#print(telefone)




