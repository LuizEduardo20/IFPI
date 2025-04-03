lista = []
listaPositivo = []
listaNegativa = []

for i in range(10):
    while True:
        try:
            valor = int(input('Diite um valor: '))
            lista.append(valor)
            
            if valor > 0:
                listaPositivo.append(valor)
            else:
                listaNegativa.append(valor)
                break
        
        except ValueError:
            print('Valor Invalido !!')

print(lista)
print(listaPositivo)
print(listaNegativa)
