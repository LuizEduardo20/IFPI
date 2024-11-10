class Veiculo:
    def __init__(self, chassi, marca, modelo, ano, placa = 'Sem placa', 
                 cor = 'Sem cor', proprietario = 'Sem proprietario', quilometragem = 0):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.proprietario = proprietario
        self.quilometragem = quilometragem

    def digitar_cor(self, cor):
        self.cor = cor

    def digitar_placa(self, placa):
        self.placa =placa

    def digitar_proprietario(self, proprietario):
        self.proprietario =proprietario

    def digitar_quilometragem(self, quilometragem):
        self.quilometragem = quilometragem


    def __str__(self):
        return '''Chassi: {},\nMarca: {},\nModelo: {},\nAno: {},\nPlaca: {},\nCor: {},\nPropriétario: {},\nQuilometragem: {}KM.'''.format(self.chassi, self.marca, self.modelo, self.ano, self.placa, self.cor, self.proprietario, self.quilometragem)

especificacoes = Veiculo('AB1234F77', 'Nissam', 'R34 Nismo', 1998)
especificacoes.digitar_cor('Azul Marinho(2f2c79)')
especificacoes.digitar_placa('AB1234')
especificacoes.digitar_proprietario('Eduardo')
especificacoes.digitar_quilometragem(21876)

print(especificacoes)
