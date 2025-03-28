def continuarPara():
    while True:
        resposta = input('Deseja continuar? (S/N): ')
        if resposta in ['S', 'N']:
            return resposta
        print('Caractere inválido. Digite novamente')

def calcular(n):
    return n ** 3

while True:
    try:
        numero = float(input('Digite um número: '))
        resultado = calcular(numero)
        print(f'O cubo de {numero} é {resultado}')
        
        if continuarPara() == 'N':
            print('Programa parou')
            break
    except ValueError:
        print('Erro! Digite um número válido')
