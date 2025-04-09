lista = []
listaPositivo = []
listaNegativa = []

def positivo_negativo(valor):
    if valor > 0:
        listaPositivo.append(valor)
    elif valor < 0:
        listaNegativa.append(valor)

for i in range(10):
    while True:
        try:
            x = int(input('Digite um valor: '))
            lista.append(x)
            positivo_negativo(x)
            break
        except ValueError:
            print('Valor Inválido!!')


print("Lista completa:", lista)
print("Lista de números positivos:", listaPositivo)
print("Lista de números negativos:", listaNegativa)
