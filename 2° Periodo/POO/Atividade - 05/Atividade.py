from datetime import datetime

class CarteiraHabilitacao:
    def __init__(self, nome_pai, observacao, nome, data_nascimento, numero_registro, 
                 nome_mae, cpf, validade, local_expedicao, validade_documento, tipo_carteira):
        self.nome_pai = nome_pai
        self.observacao = observacao
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.numero_registro = numero_registro
        self.nome_mae = nome_mae
        self.cpf = cpf
        self.validade = validade
        self.local_expedicao = local_expedicao
        self.validade_documento = validade_documento
        self.tipo_carteira = tipo_carteira
        
        self.verificar_atributos_obrigatorios()
        
    def verificar_atributos_obrigatorios(self):
        atributos_obrigatorios = ['nome_pai', 'observacao', 'nome', 'data_nascimento', 
                                  'numero_registro', 'nome_mae', 'cpf', 'validade', 
                                  'local_expedicao', 'validade_documento', 'tipo_carteira']
        
        for atributo in atributos_obrigatorios:
            if not hasattr(self, atributo):
                raise ValueError(f"Faltou fornecer o atributo obrigatório: {atributo}")
        
    def __str__(self):
        return f"Carteira de Habilitação\nTipo: {self.tipo_carteira}\nNome: {self.nome}\nObservação: {self.observacao}\n" \
               f"Número do Registro: {self.numero_registro}\nCPF: {self.cpf}\n" \
               f"Validade: {self.validade}\nLocal de Expedição: {self.local_expedicao}\n" \
               f"Validade do Documento: {self.validade_documento}"

try:
    carteira = CarteiraHabilitacao("João", "Sem observações", "Maria", "01/01/1990",
                                   "R123456", "Ana", "123.456.789-00", 
                                   "31/12/2030", "São Paulo", "31/12/2025", "A")
    print(carteira)
except ValueError as e:
    print(f"Erro: {e}")
