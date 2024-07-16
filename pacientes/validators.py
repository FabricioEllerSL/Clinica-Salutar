import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos

    if len(cpf) != 11:
        return False

    # Calcula os dígitos verificadores
    def calcula_digito(digitos):
        soma = 0
        peso = len(digitos) + 1
        for digito in digitos:
            soma += int(digito) * peso
            peso -= 1
        resto = 11 - (soma % 11)
        return str(resto if resto < 10 else 0)

    if cpf == cpf[0] * 11:
        return False

    digito1 = calcula_digito(cpf[:9])
    digito2 = calcula_digito(cpf[:9] + digito1)
    
    return cpf[-2:] == digito1 + digito2
