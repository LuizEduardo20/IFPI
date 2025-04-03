#Implemente a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual,
#altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela,
#calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).

class Bicicleta:
    MAX_VELOCIDADE = 50
    MIN_VELOCIDADE = 0
    MAX_ALTURA_CELA = 200
    MIN_ALTURA_CELA = 0
    MAX_CALIBRAGEM_PNEUS = 100
    MIN_CALIBRAGEM_PNEUS = 0

    def __init__(self, velocidade=0, altura_cela=0, calibragem_pneus=0):
        self._velocidade = velocidade
        self._altura_cela = altura_cela
        self._calibragem_pneus = calibragem_pneus

    def velocidade(self):
        return self._velocidade

    def velocidade(self, valor):
        if self.MIN_VELOCIDADE <= valor <= self.MAX_VELOCIDADE:
            self._velocidade = valor
        else:
            print("Velocidade fora dos limites permitidos")

    def altura_cela(self):
        return self._altura_cela

    def altura_cela(self, valor):
        if self.MIN_ALTURA_CELA <= valor <= self.MAX_ALTURA_CELA:
            self._altura_cela = valor
        else:
            print("Altura da cela fora dos limites permitidos")

    def calibragem_pneus(self):
        return self._calibragem_pneus

    def calibragem_pneus(self, valor):
        if self.MIN_CALIBRAGEM_PNEUS <= valor <= self.MAX_CALIBRAGEM_PNEUS:
            self._calibragem_pneus = valor
        else:
            print("Calibragem de pneus fora dos limites permitidos")

    def regular_cela(self):
        if self.velocidade == 0:
            self.altura_cela = 80
            print("Cela foi Ajustada!")
        else:
            print("Não é possível regular a cela enquanto a bicicleta está em movimento.")

    def calibrar_pneus(self):
        if self.velocidade == 0:
            self.calibragem_pneus = 75
            print("Pneus foram Calibrados!")
        else:
            print("Não é possível calibrar os pneus enquanto a bicicleta está em movimento.")

def main():
    bicicleta = Bicicleta()

    bicicleta.velocidade = 10
    bicicleta.altura_cela = 100
    bicicleta.calibragem_pneus = 90
    bicicleta.regular_cela()
    bicicleta.calibrar_pneus()

if __name__ == '__main__':
    main()
