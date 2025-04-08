lista = []

for i in range(15):
    while True:
        try:
            valor = int(input(f"Digite o {i+1}º elemento da lista: "))
            lista.append(valor)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

maior = lista[0]
posicao_maior = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posicao_maior = i

menor = lista[0]
posicao_menor = 0

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        posicao_menor = i

print(f"O maior elemento é {maior} e está na posição {posicao_maior}")
print(f"O menor elemento é {menor} e está na posição {posicao_menor}")
