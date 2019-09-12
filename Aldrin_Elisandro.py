import re

entradadata = input('Digite a data\n')
entradaemail = input('Digite o email\n')
patterndata = '^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$'
resultadodata = re.search(patterndata, entradadata)

patternemail = '^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$'
resultadoemail = re.search(patternemail, entradaemail)

if resultadodata == None:
    print('A data e invalida')
else:
    print('A data e: ' + resultadodata.group())

if resultadoemail == None:
    print('O email e invalida')
else:
    print('O email e: ' + resultadoemail.group())
