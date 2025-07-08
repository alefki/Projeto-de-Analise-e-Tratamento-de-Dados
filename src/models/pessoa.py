class Pessoa:
    def __init__(self, **kwargs):
        self.nome_completo = kwargs.get('nome_completo', '')
        self.idade = kwargs.get('idade', None)
        self.cep = kwargs.get('cep', '')
        self.celular = kwargs.get('celular', '')
        
        self.primeiro_nome = ''
        self.segundo_nome = ''
        self.genero = ''
        self.logradouro = ''
        self.bairro = ''
        self.cidade = ''
        self.estado = ''
        
        self.observacoes = []

    def adicionar_observacao(self, observacao):
        self.observacoes.append(observacao)

    def to_dict(self):
        return {
            "Nome Completo": self.nome_completo,
            "Idade": self.idade,
            "Primeiro Nome": self.primeiro_nome,
            "Segundo Nome": self.segundo_nome,
            "Gênero": self.genero,
            "CEP Original": self.cep,
            "Logradouro": self.logradouro,
            "Bairro": self.bairro,
            "Cidade": self.cidade,
            "Estado": self.estado,
            "Celular": self.celular,
            "Observacoes": ", ".join(self.observacoes)
        }
    
