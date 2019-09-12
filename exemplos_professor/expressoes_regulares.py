import re
'''
Explicações:
o 'r' é para RAW String
Ex: 
print('Olá, Mundo!\nTudo Bem?')
print(r'Olá, Mundo!\nTudo Bem?')
'''

# 1
texto = 'Eu sou programador!'
# pattern = r'gr' # Exemplo 01 - Texto simples
# pattern = r'so\w' # Exemplo 02 - Letra (não pode ser espaço vazio)
pattern = r'\w\w\w' # Exemplo 03 - 1° palavra com 3 letras
resultado = re.search(pattern, texto)
if resultado:
	print(resultado.group())
else:
	print('Padrao Não encontrado!')

# 2
texto = 'O rato roeu a roupa do rei de Roma!'
pattern = r'r\w' # Exemplo 01
pattern = r'r\w+' # Exemplo 02
pattern = r'(?i)r\w+' # Exemplo 02 - Ignora Case
pattern = r'[ro]' # Exemplo 02 - Procura por um conjunto de letras
pattern = r'[ro]+' # Exemplo 02 - Procura por um conjunto de letras
pattern = r'[ro]+\w' # Exemplo 02 - Procura por um conjunto de letras
pattern = r'[ro]+\w+' # Exemplo 02 - Procura por um conjunto de letras
resultado = re.findall(pattern, texto)
if resultado:
	print(resultado)
else:
	print('Padrao Não encontrado!')

# 3
texto = 'banana,maça,uva,laranja'
pattern = r','
resultado = re.split(pattern, texto)
print(resultado)

# Vamos praticar no site: https://regex101.com/