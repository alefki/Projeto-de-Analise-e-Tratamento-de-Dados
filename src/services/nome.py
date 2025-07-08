import requests

class NomeService:
    def __init__(self):
        self.gender_cache = {}
        self.api_key = ""

    def extrair_primeiro_e_segundo_nome(self, nome_completo):
        if not isinstance(nome_completo, str):
            return "", ""
        partes = nome_completo.split()
        primeiro_nome = partes[0] if partes else ""
        segundo_nome = partes[1] if len(partes) > 1 else ""
        return primeiro_nome, segundo_nome

    def determinar_genero(self, primeiro_nome):
        if not primeiro_nome:
            return "unknown"

        primeiro_nome_lower = primeiro_nome.lower()

        if primeiro_nome_lower in self.gender_cache:
            return self.gender_cache[primeiro_nome_lower]

        try:
            url = f"https://api.genderize.io/?name={primeiro_nome_lower}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            genero = data.get("gender")
            if genero is None:
                genero = "unknown"

            self.gender_cache[primeiro_nome_lower] = genero

            return genero
        except requests.exceptions.RequestException as e:
            return "unknown"
        
        