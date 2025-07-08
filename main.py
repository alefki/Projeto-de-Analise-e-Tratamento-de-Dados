import pandas as pd
from src.models.pessoa import Pessoa
from src.services.nome import NomeService
from src.services.cep import CEPService
from src.services.celular import CelularService

class ProcessadorDeDados:
    def __init__(self):
        self.nome_service = NomeService()
        self.cep_service = CEPService()
        self.celular_service = CelularService()

    def processar_dados(self, caminho_entrada, caminho_saida):
        try:
            df = pd.read_csv(caminho_entrada, encoding='utf-8')
            
            pessoas_processadas = []

            for index, row in df.iterrows():
                pessoa = Pessoa(
                    nome_completo=row.get('Nome Completo', ''), 
                    idade=row.get('Idade', None),              
                    cep=row.get('CEP', ''),
                    celular=row.get('Celular', '')
                )
                
                primeiro_nome, segundo_nome = self.nome_service.extrair_primeiro_e_segundo_nome(pessoa.nome_completo)
                pessoa.primeiro_nome = primeiro_nome
                pessoa.segundo_nome = segundo_nome
                
                if primeiro_nome:
                    genero = self.nome_service.determinar_genero(primeiro_nome)
                    pessoa.genero = genero
                    if genero == "unknown":
                        pessoa.adicionar_observacao(f"Gênero desconhecido para '{primeiro_nome}'")
                else:
                    pessoa.adicionar_observacao("Nome completo vazio, gênero não determinado.")

                if pessoa.cep:
                    endereco_data = self.cep_service.buscar_endereco_por_cep(pessoa.cep)
                    if endereco_data:
                        pessoa.logradouro = endereco_data.get('logradouro', '')
                        pessoa.bairro = endereco_data.get('bairro', '')
                        pessoa.cidade = endereco_data.get('localidade', '')
                        pessoa.estado = endereco_data.get('uf', '')
                    else:
                        pessoa.adicionar_observacao(f"CEP '{pessoa.cep}' inválido ou não encontrado.")
                else:
                    pessoa.adicionar_observacao("CEP vazio, endereço não buscado.")

                estado_do_cep = pessoa.estado
                celular_normalizado, obs_celular = self.celular_service.normalizar_celular(pessoa.celular, estado_do_cep)
                
                pessoa.celular = celular_normalizado
                if obs_celular:
                    pessoa.adicionar_observacao(obs_celular)

                pessoas_processadas.append(pessoa)
            
            df_saida = pd.DataFrame([p.to_dict() for p in pessoas_processadas])
            
            df_saida.to_csv(caminho_saida, index=False, encoding='utf-8')
            
            print(f"Dados processados e salvos em: {caminho_saida}")

        except FileNotFoundError:
            print(f"Erro: O arquivo de entrada '{caminho_entrada}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    processador = ProcessadorDeDados()
    
    input_file_path = "lista_clientes.csv" 
    output_file_path = "dados_enriquecidos.csv"
    
    processador.processar_dados(input_file_path, output_file_path)

