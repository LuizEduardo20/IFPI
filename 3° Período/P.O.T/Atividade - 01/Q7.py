def fatorial(n):
    if n == 0 or n == 1:
        return 1
    
    elif n > 0:
        return n * fatorial(n - 1)
    
    else:
        print('Valor inválido!!')

while True:
    try:
        numero = int(input('Fatorial de: '))
        if numero >= 0:
            break

        else:
            print('Digite um número inteiro!')

    except ValueError:
        print('Erro de valor!!')

resultado = fatorial(numero)
print(f'O fatorial de {numero} é: {resultado}')
