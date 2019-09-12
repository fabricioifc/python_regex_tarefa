# coding: utf-8
import re

texto = 'Carla tem 15 anos, Pedro tem 16 e Aline tem 30.'
pattern_idades = r'\d{1,2}'
pattern_nomes = '[A-Z][a-z]*'

idades = re.findall(pattern_idades, texto)
nomes = re.findall(pattern_nomes, texto)

print(idades)
print(nomes)


dicionario_dados = {}
indice = 0
for nome in nomes:
	dicionario_dados[nome] = idades[indice]
	indice+=1
print(dicionario_dados)