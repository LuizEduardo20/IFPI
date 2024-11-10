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

    def __str__(self):
        return '''Chassi: {},\nMarca: {},\nModelo: {},\nAno: {},\nPlaca: {},\nCor: {},\nPropriétario: {},\nQuilometragem: {}KM.'''.format(self.chassi, self.marca, self.modelo, self.ano, self.placa, self.cor, self.proprietario, self.quilometragem)

especificacoes = Veiculo('AB1234F77', 'Nissam', 'R34 Nismo', 1998, 'AB1234', 'Azul Marinho(2f2c79)', 'Eduardo', 23185)

print(str(especificacoes))
