def inserir_elementos(lista, nome_lista):
    for i in range(10):
        while True:
            try:
                elemento = int(input(f'Digite o {i+1}º elemento da {nome_lista}: '))
                lista.append(elemento)
                break
            except ValueError:
                print('Erro!! Digite apenas números inteiros')

def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(10):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada

lista1 = []
lista2 = []

inserir_elementos(lista1, "primeira lista")
inserir_elementos(lista2, "segunda lista")

lista_intercalada = intercalar_listas(lista1, lista2)

print('\nPrimeira lista:', lista1)
print('Segunda lista:', lista2)
print('Lista intercalada:', lista_intercalada)
