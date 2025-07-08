import re

class CPFService:
    def limpar_cpf(self, cpf):
        if not isinstance(cpf, str):
            return ""
        return re.sub(r'\D', '', cpf)

    def eh_valido(self, cpf):
        cpf = self.limpar_cpf(cpf)

        if not cpf or len(cpf) != 11 or not cpf.isdigit():
            return False

        if len(set(cpf)) == 1:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = 11 - (soma % 11)
        if digito1 > 9:
            digito1 = 0

        if not (int(cpf[9]) == digito1):
            return False

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = 11 - (soma % 11)
        if digito2 > 9:
            digito2 = 0

        # Verifica o segundo dígito
        if not (int(cpf[10]) == digito2):
            return False

        return True