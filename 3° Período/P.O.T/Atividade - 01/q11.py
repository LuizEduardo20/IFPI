def divisores(n):
    if n <= 0:
        print('Digite um valor positivo!!')
    
    contador = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
    
    return contador

while True:
    try:
        numero = int(input('Digite um valor: '))
        if numero == 0:
            print('Programa Finalizado!')
            break
        
        resultado = divisores(numero)
        print(f'O Numero {numero} tem {resultado} divisores')
        
    except ValueError:
        print('Erro de valor!!')
