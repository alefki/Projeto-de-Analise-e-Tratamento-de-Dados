import os
import requests

def _chamar_api_genderize(primeiro_nome):
    try:
        response = requests.get(f"https://api.genderize.io/?name={primeiro_nome}")
        response.raise_for_status()
        data = response.json()
        return data.get('gender')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar Genderize.io: {e}")
        return None

def _chamar_api_gender_api_com(primeiro_nome):
    api_key = os.getenv('GENDERAPI_COM_KEY')
    if not api_key:
        print("Erro: Variável de ambiente GENDERAPI_COM_KEY não configurada.")
        return None
    headers = {'X-Auth-Token': api_key}
    try:
        response = requests.get(f"https://gender-api.com/get?name={primeiro_nome}&key={api_key}", headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('gender')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar Gender-API.com: {e}")
        return None

def _chamar_api_gender_api_io(primeiro_nome):
    api_key = os.getenv('GENDERAPI_IO_KEY')
    if not api_key:
        print("Erro: Variável de ambiente GENDERAPI_IO_KEY não configurada.")
        return None
    try:
        response = requests.get(f"https://genderapi.io/api/?name={primeiro_nome}&key={api_key}")
        response.raise_for_status()
        data = response.json()
        return data.get('gender')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar Genderapi.io: {e}")
        return None

def inferir_genero(pessoa, api_preferencial=None):
    if not pessoa.primeiro_nome:
        pessoa.observacoes.append("Primeiro nome ausente para inferência de gênero.")
        return

    primeiro_nome = pessoa.primeiro_nome

    apis = {
        'genderize.io': _chamar_api_genderize,
        'gender-api.com': _chamar_api_gender_api_com,
        'genderapi.io': _chamar_api_gender_api_io
    }

    if api_preferencial and api_preferencial in apis:
        genero = apis[api_preferencial](primeiro_nome)
        if genero:
            pessoa.genero = genero
            return

    for api_nome, api_func in apis.items():
        if api_nome == api_preferencial:
            continue
        genero = api_func(primeiro_nome)
        if genero:
            pessoa.genero = genero
            return

    pessoa.observacoes.append(f"Não foi possível inferir gênero para '{primeiro_nome}' com as APIs disponíveis.")

    