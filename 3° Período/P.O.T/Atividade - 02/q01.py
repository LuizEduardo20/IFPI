lista = []
listaPar = []
listaImpar = []

for i in range(100):
    while True:
        try:
            valor = int(input("Digite um valor: "))
            lista.append(valor)
            
            if valor % 2 == 0:
                listaPar.append(valor)
            else:
                listaImpar.append(valor)
                break
            
        except ValueError:
            print("Valor invalido")

print(lista)
print(listaPar)
print(listaImpar)
