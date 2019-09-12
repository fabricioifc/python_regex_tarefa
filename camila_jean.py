# coding: utf-8
import re

nome = str(input('Informe um nome válido '))
cpf = str(input('Informe um cpf válido '))
matricula = str(input('Informe a matrícula '))

pattern = '([A-Z][a-z]+\s[A-Z][a-z]+)'
resultado = re.search(pattern, nome)

pattern = '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'
retorno = re.match(pattern, cpf)

pattern = '(19|20)\d{8}'
resposta = re.match(pattern, matricula)

print(resultado)
print(retorno)
print(resposta)

#match deve ser igual
#search faz uma pesquisa
#findall vai pesquisar  uma lista -  traz uma lista
