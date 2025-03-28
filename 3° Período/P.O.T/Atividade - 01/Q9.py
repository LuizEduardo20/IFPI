def somar(n1, n2):
    resultado = n1 + n2
    print(f'A soma de {n1} + {n2} = {resultado}')
    
while True:
    try:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
        resultad = somar(numero1, numero2)
    
    except ValueError:
        print('Erro de valor!')
