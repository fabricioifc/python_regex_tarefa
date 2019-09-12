import re

string_nome = input('Informe o Matricula do aluno')

padrao = re.search(r'(19|20)\d{8}', string_nome)

if padrao is None:
	print("padrao nao encontrado")
else:
	print(padrao.group())	

string_cpf = input('informe o cpf')

resultado = re.search(r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}', string_cpf)
if resultado is None:
	print("cpf n encontrado")
else:
	print(resultado.group()) 