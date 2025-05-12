def intercalar_listas(lista1, lista2):
    lista_intercalada = []

    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

    return lista_intercalada

def main():
    lista1 = [1, 3, 5, 7, 9]
    lista2 = [2, 4, 6, 8, 10]
    lista_intercalada = intercalar_listas(lista1, lista2)
    assert lista_intercalada == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    lista1 = [10, 20, 30]
    lista2 = [40, 50, 60]
    lista_intercalada = intercalar_listas(lista1, lista2)
    assert lista_intercalada == [10, 40, 20, 50, 30, 60]
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
