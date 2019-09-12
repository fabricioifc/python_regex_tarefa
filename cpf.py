import re

usuario_cpf = str(input("Informe o numero do cpf: ")

pattern = '/^([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}|[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})$/'


if re.match(usuario_cpf):
    print(usuario_cpf + "É um CPF Válido")
else:
    print(usuario_cpf + "É um CPF Inválido")

