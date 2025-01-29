class RadioFM:
    def __init__(self, estacoes):
        self._volume_min = 0
        self._volume_max = estacoes['volume_max']
        self._freq_min = 88
        self._freq_max = 108
        self._estacoes = estacoes
        self._volume = None
        self._ligado = False
        self._estacao_atual = None
        self._frequencia_atual = None
        self._antena_habilitada = False

    @property
    def ligado(self):
        return self._ligado

    @property
    def volume(self):
        return self._volume

    @property
    def frequencia_atual(self):
        return self._frequencia_atual

    @property
    def estacao_atual(self):
        return self._estacao_atual

    def ligar(self):
        self._ligado = True
        self._volume = self._volume_min
        if self._antena_habilitada:
            self._frequencia_atual = list(self._estacoes.keys())[0]
            self._estacao_atual = self._estacoes[self._frequencia_atual]

    def desligar(self):
        self._ligado = False
        self._volume = None
        self._frequencia_atual = None
        self._estacao_atual = None

    def aumentar_volume(self, incremento=1):
        if self._ligado:
            self._volume = min(self._volume + incremento, self._volume_max)

    def diminuir_volume(self, decremento=1):
        if self._ligado:
            self._volume = max(self._volume - decremento, self._volume_min)

    def mudar_frequencia(self, frequencia=None):
        if self._ligado:
            if frequencia is None:
                frequencias = list(self._estacoes.keys())
                indice_atual = frequencias.index(self._frequencia_atual)
                self._frequencia_atual = frequencias[(indice_atual + 1) % len(frequencias)]
                self._estacao_atual = self._estacoes[self._frequencia_atual]
            else:
                if frequencia in self._estacoes:
                    self._frequencia_atual = frequencia
                    self._estacao_atual = self._estacoes[frequencia]
                else:
                    self._frequencia_atual = frequencia
                    self._estacao_atual = 'estação inexistente'

radio1 = RadioFM({'89.5': 'Cocais', '91.5': 'Mix', '94.1': 'Boa', '99.1': 'Clube', 'volume_max': 20})

radio1.ligar()
print(f"Rádio 1 ligado: {radio1.ligado}")
print(f"Volume do Rádio 1: {radio1.volume}")
print(f"Frequência atual do Rádio 1: {radio1.frequencia_atual}")
print(f"Estação atual do Rádio 1: {radio1.estacao_atual}")

radio1.aumentar_volume(5)
print(f"Volume do Rádio 1: {radio1.volume}")

radio1.diminuir_volume(3)
print(f"Volume do Rádio 1: {radio1.volume}")

radio1.mudar_frequencia(94.1)
print(f"Frequência atual do Rádio 1: {radio1.frequencia_atual}")
print(f"Estação atual do Rádio 1: {radio1.estacao_atual}")

radio1.desligar()
print(f"Rádio 1 ligado: {radio1.ligado}")
print(f"Volume do Rádio 1: {radio1.volume}")
print(f"Frequência atual do Rádio 1: {radio1.frequencia_atual}")
print(f"Estação atual do Rádio 1: {radio1.estacao_atual}")
