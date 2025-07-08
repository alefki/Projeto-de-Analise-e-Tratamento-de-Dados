import csv

def ler_csv(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dados.append(row)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o CSV: {e}")
    return dados