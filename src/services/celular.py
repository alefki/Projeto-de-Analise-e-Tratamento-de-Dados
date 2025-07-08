class CelularService:
    def __init__(self):
        self.ddd_por_estado = {
            "AC": ["68"], "AL": ["82"], "AM": ["97", "92"], "AP": ["96"],
            "BA": ["71", "73", "74", "75", "77"], "CE": ["85", "88"], "DF": ["61"],
            "ES": ["27", "28"], "GO": ["62", "64", "61"], "MA": ["98", "99"],
            "MG": ["31", "32", "33", "34", "35", "37", "38"], "MS": ["67"],
            "MT": ["65", "66"], "PA": ["91", "93", "94"], "PB": ["83"],
            "PE": ["81", "87"], "PI": ["86", "89"], "PR": ["41", "42", "43", "44", "45", "46"],
            "RJ": ["21", "22", "24"], "RN": ["84"], "RO": ["69"], "RR": ["95"],
            "RS": ["51", "53", "54", "55"], "SC": ["47", "48", "49"], "SE": ["79"],
            "SP": ["11", "12", "13", "14", "15", "16", "17", "18", "19"], "TO": ["63"]
        }

    def normalizar_celular(self, numero_celular, estado_origem=None):
        if not numero_celular:
            return "", "Esse usuário não inseriu um número"

        apenas_digitos = "".join(c for c in str(numero_celular) if c.isdigit())
        observacao = ""
        ddd = ""
        numero_formatado = ""

        if len(apenas_digitos) <= 7:
            return "", "Número incompleto"

        if len(apenas_digitos) == 8:
            numero_formatado = "9" + apenas_digitos
            if estado_origem:
                ddds_possiveis = self.ddd_por_estado.get(estado_origem.upper(), [])
                if ddds_possiveis:
                    ddd = ddds_possiveis[0]
                else:
                    observacao = "Não foi possível inferir o DDD pelo estado."
            else:
                observacao = "DDD ausente e estado não fornecido para inferência."
            return f"{ddd} {numero_formatado}".strip(), observacao.strip()

        if len(apenas_digitos) == 9:
            if estado_origem:
                ddds_possiveis = self.ddd_por_estado.get(estado_origem.upper(), [])
                if ddds_possiveis:
                    ddd = ddds_possiveis[0]
                else:
                    observacao = "Não foi possível inferir o DDD pelo estado."
            else:
                observacao = "DDD ausente e estado não fornecido para inferência."
            return f"{ddd} 9{apenas_digitos}".strip(), observacao.strip()

        if len(apenas_digitos) == 10:
            ddd = apenas_digitos[:2]
            numero_formatado = "9" + apenas_digitos[2:]
            return f"{ddd} {numero_formatado}", ""

        if len(apenas_digitos) == 11:
            ddd = apenas_digitos[:2]
            numero_formatado = apenas_digitos[2:]
            return f"{ddd} {numero_formatado}", ""

        return apenas_digitos, "Formato de número desconhecido."