lista1 = []
lista2 = []

for i in range(10):
    while True:
        try:
            elemento = int(input(f'Digite o {i+1}º elemento da primeira lista: '))
            lista1.append(elemento)
            break

        except ValueError:
            print('Erro!! Digite apenas números inteiros')

for i in range(10):
    while True:
        try:
            elemento = int(input(f'Digite o {i+1}º elemento da segunda lista: '))
            lista2.append(elemento)
            break

        except ValueError:
            print('Erro!! Digite apenas números inteiros')

lista_intercalada = []

for i in range(10):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

print('\nPrimeira lista:', lista1)
print('Segunda lista:', lista2)
print('Lista intercalada:', lista_intercalada)
