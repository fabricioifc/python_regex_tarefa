import re

usuario_cpf = input("Informe o numero do cpf: ")

pattern_int = re.compile(r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")


if pattern_int.match(usuario_cpf):
    print(usuario_cpf + "É um CPF Válido")
else:
    print(usuario_cpf + "É um CPF Inválido")

