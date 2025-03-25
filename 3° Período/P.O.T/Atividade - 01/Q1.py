numero = int(input('Digita um valor legal ai!!'))

def verificar_numero(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

resultado = verificar_numero(numero)

print(f"O número {numero} é {resultado}.")
