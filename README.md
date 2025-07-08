# Projeto 8 - Análise de Dados

## Visão Geral do Projeto

Este projeto tem como objetivo principal a normalização e enriquecimento de dados de uma lista de clientes fornecida em formato CSV. Ele utiliza os princípios da Programação Orientada a Objetos (POO) para estruturar o código em módulos claros e testáveis, interagindo com APIs externas para inferência de gênero e busca de informações de CEP. O resultado do processamento é um novo arquivo CSV com os dados normalizados e enriquecidos, incluindo observações sobre quaisquer problemas encontrados.

## Funcionalidades Implementadas

O sistema atualmente implementa as seguintes funcionalidades:

### 1. Normalização de Nomes

* **Extração:** Separa o nome completo em "Primeiro Nome" e "Segundo Nome".
* **Inferência de Gênero:** Utiliza a API Genderize.io para inferir o gênero (masculino, feminino, ou desconhecido) a partir do primeiro nome.

### 2. Normalização de CEP

* **Limpeza:** Remove caracteres não numéricos, garantindo que o CEP contenha apenas 8 dígitos.
* **Enriquecimento Geográfico:** Utiliza a API ViaCEP para obter e adicionar informações de "Logradouro", "Bairro", "Cidade" e "Estado" com base no CEP fornecido.
* **Tratamento de CEPs Inválidos:** Registra uma observação se o CEP for inválido ou não encontrado.

### 3. Normalização de Celular

* **Limpeza:** Remove caracteres não numéricos do número do celular.
* **Formatação:** Garante o formato "DD 9XXXXXXXX", adicionando o dígito '9' quando necessário.
* **Inferência de DDD:** Tenta inferir o DDD com base no Estado obtido via CEP, se o DDD estiver ausente no número original.
* **Tratamento de Números Incompletos/Ausentes:** Adiciona observações específicas para números com menos de 8 dígitos ou campos de celular vazios.

### 4. Gerenciamento de Observações

* Um campo "Observacoes" é adicionado a cada registro, consolidando todos os problemas e informações relevantes detectados durante o processo de normalização para o respectivo cliente.

## Estrutura do Projeto

A estrutura de diretórios do projeto segue um padrão modular para organização e clareza:

.
├── src/                          # Código-fonte da aplicação
│   ├── models/                   # Classes que representam entidades de negócio (ex: Pessoa)
│   │   └── pessoa.py
│   └── services/                 # Regras de negócio que dependem de recursos externos ou lógicas complexas
│       ├── cep.py
│       ├── celular.py
│       └── nome.py
├── tests/                        # Testes unitários para os módulos de serviço
│   ├── test_cep.py
│   └── test_nome.py
├── lista_clientes.csv            # Arquivo de entrada com os dados dos clientes
├── dados_enriquecidos.csv        # Arquivo de saída com os dados processados e enriquecidos
└── main.py                       # Ponto de entrada principal do script que orquestra as operações


## Como Executar

Para executar este projeto, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.7 ou superior é recomendada).
Instale as bibliotecas necessárias usando `pip`:

```bash
pip install pandas requests
Arquivo de Entrada
O projeto espera um arquivo CSV chamado lista_clientes.csv na raiz do projeto. Este arquivo deve conter, no mínimo, as colunas Nome Completo, Idade e CEP, e opcionalmente a coluna Celular.

Exemplo de lista_clientes.csv:

Snippet de código

Nome Completo,Idade,CEP,Celular
João da Silva,30,01001-000,9876543
Maria Souza,25,20010-000,99887766
Execução
Navegue até o diretório raiz do projeto no seu terminal.

Execute o script main.py:

Bash

python main.py
Após a execução, um novo arquivo CSV chamado dados_enriquecidos.csv será gerado na raiz do projeto, contendo os dados original e as novas colunas enriquecidas.

Testes
Para executar os testes unitários do projeto, utilize o seguinte comando na raiz do projeto:

Bash

python -m unittest tests/test_nome.py
python -m unittest tests/test_cep.py
Próximos Passos (Funcionalidades a serem implementadas)
Implementação do serviço de CPF (formatação, validação e observações).

Formatação Camel Case e tratamento mais robusto de sobrenomes compostos para nomes.

Integração com múltiplas APIs de gênero para fallback e seleção da melhor.

Leitura de API Keys de variáveis de ambiente.

Geração de arquivo de saída no formato JSON.

Criação de um módulo para geração de relatórios de análise de dados (distribuição de gênero, geográfica, qualidade dos dados, áreas de interesse).

Refatoração da leitura e escrita de dados para um módulo src/repo/ dedicado.
