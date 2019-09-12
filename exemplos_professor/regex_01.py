# coding: utf-8
# Site validador: https://pythex.org/
import re

nome = 'Fabricio Bizotto'
matricula = '2018006563'
cpf = '067.569.199-03'
dtnascimento = '19/05/1989'
texto = 'Uma expressão regular (RegEx) é uma sequência de caracteres que define um padrão de pesquisa'

def is_vazio(texto):
	return texto.__eq__('')

def is_valido(regex):
	# print(regex)
	return False if regex is None else True

def validar_matricula(numero):
	matricula_pattern = r'(\b(19|20)\d{2})(\d{6}\b)'
	valido = re.match(matricula_pattern, numero)
	return is_valido(valido)

def validar_texto_sem_numero(texto):
	pattern = r'\d+'
	existem_numeros = re.findall(pattern, texto)
	valido = len(existem_numeros) == 0
	return is_valido(valido)

def validar_texto_capitalizado(texto):
	pattern = r'([A-Z][a-z]+)'
	texto_dividido = dividir_texto(texto)
	for t in texto_dividido:
		valido = re.match(pattern, t)
		if not is_valido(valido):
			return False
	return True

def dividir_texto(texto):
	pattern = r'\s'
	texto_dividido = re.split(pattern, texto)
	return texto_dividido

def validar_nome_completo(texto) -> bool:
	texto_dividido = dividir_texto(texto)
	espacos_em_branco = len(texto_dividido)
	valido = True if espacos_em_branco > 1 else False
	return is_valido(valido)

def validar_cpf(numero) -> bool:
	pattern = r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'
	valido = re.match(pattern, numero)
	return is_valido(valido)

def validar_data(data) -> bool:
	pattern = r'\d{2}/\d{2}/\d{4}'
	# data_pattern = '[0-9]{2}\/?[0-9]{2}\/?[0-9]{4}'
	valido = re.match(pattern, data)
	return is_valido(valido)
		

# while is_vazio(nome):
# 	nome = str(input('Qual é o seu nome completo?\n'))

# while is_vazio(matricula):
# 	matricula = str(input('Informe seu número de matrícula:\n'))

# while is_vazio(cpf):
# 	cpf = str(input('Informe seu número de cpf (com pontuação):\n'))

# while is_vazio(dtnascimento):
# 	cpf = str(input('Informe sua data de nascimento (dd/mm/yyyy):\n'))	
	
print('Meu nome é {}'.format(nome))
print('Minha matrícula é {}'.format(matricula))
print('Meu cpf é {}'.format(cpf))
print('Minha data de nascimento é {}'.format(dtnascimento))

print('****************************************')
print('***************Validações***************')
print('****************************************')
print(validar_matricula(matricula))
print(validar_nome_completo(nome))
print(validar_texto_capitalizado(nome))
print(validar_texto_sem_numero(nome))
print(validar_cpf(cpf))
print(validar_data(dtnascimento))