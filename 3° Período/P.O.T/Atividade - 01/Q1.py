def verificar_numero(numero):
    if numero % 2 == 0:
        return 'par'
    
    else:
        return 'ímpar'

while True:
    try:
        numero = int(input('Digite um valor inteiro: '))
        break
    except ValueError:
        print('Erro: Por favor, digite apenas números inteiros!')

resultado = verificar_numero(numero)

print(f"O número {numero} é {resultado}.")
