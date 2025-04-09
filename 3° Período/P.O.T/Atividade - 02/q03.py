lista = []
lista_invertida = []

for i in range(10):
    while True:
        try:
            valor = int(input('Digite um valor: '))
            lista.append(valor)
            break
        except ValueError:
            print('Valor Invalido !!')
            
            
def inverso():
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    print(lista_invertida)
    
inverso()
