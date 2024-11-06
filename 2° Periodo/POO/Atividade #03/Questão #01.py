from datetime import datetime

class Relógio_Digital_Simples:
    horas = 0
    minutos = 0
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos
    
    def mudar_horas(self, horas):
        self.horas = horas
    
    def mudar_minutos(self, minutos):
        self.minutos = minutos

def main():
    hora_atual = Relógio_Digital_Simples(9, 32)
    #Na linha 24 e 25, o comando vai pegar a hora e os minutos atuais no computador
    hora_atual.mudar_horas(datetime.now().strftime('%H'))
    hora_atual.mudar_minutos(datetime.now().strftime('%M'))
    #Se quiser alterar a hora manualmente, apenas comente essas duas linhas, assim, ele vai imprimir os
    #valores da linha 22
    print('Hora:', hora_atual.horas)
    print('Minutos:', hora_atual.minutos)


if __name__ == '__main__':
    main()
