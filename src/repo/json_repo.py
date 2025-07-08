import json

def salvar_json(lista_pessoas, caminho_arquivo):
    dados_para_json = []
    for pessoa in lista_pessoas:
        pessoa_dict = pessoa.to_dict()
        dados_para_json.append(pessoa_dict)

    try:
        saida_final = {"users": dados_para_json} 
        with open(caminho_arquivo, mode='w', encoding='utf-8') as file:
            json.dump(saida_final, file, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{caminho_arquivo}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o JSON: {e}")