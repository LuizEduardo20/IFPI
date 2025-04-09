lista = []
listaPar = []
listaImpar = []

for i in range(5):
    while True:
        try:
            x = int(input("Digite um valor: "))
            lista.append(x)
            break
            
        except ValueError:
            print("Valor invalido")

def impa_par(valor):
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
for i in range(len(lista)):       
    impa_par(lista[i])

print(lista)
print(listaImpar)
print(listaPar)

