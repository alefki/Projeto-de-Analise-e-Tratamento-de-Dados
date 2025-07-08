import requests

class CEPService:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/"
        self.cep_cache = {}

    def buscar_endereco_por_cep(self, cep):
        cep_somente_numeros = ""
        for caractere in cep:
            if caractere.isdigit():
                cep_somente_numeros += caractere

        if len(cep_somente_numeros) != 8:
            return None

        if cep_somente_numeros in self.cep_cache:
            return self.cep_cache[cep_somente_numeros]

        try:
            url_completa = f"{self.base_url}{cep_somente_numeros}/json/"
            resposta = requests.get(url_completa)

            if resposta.status_code == 200:
                dados_endereco = resposta.json()

                if "erro" in dados_endereco and dados_endereco["erro"] == True:
                    return None
                else:
                    self.cep_cache[cep_somente_numeros] = dados_endereco
                    return dados_endereco
            else:
                return None

        except requests.exceptions.RequestException:
            return None
        
        