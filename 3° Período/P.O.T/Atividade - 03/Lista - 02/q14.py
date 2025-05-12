def modificar_lista(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0

    return lista

def main():
    lista_C = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    lista_modificada = modificar_lista(lista_C)
    
    assert lista_modificada == [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
    assert lista_modificada == [0, 4, 3, 6, 0, 3, 8, 1, 2, 2]
    assert lista_modificada == [2, 1, 6, 5, 8, 1, 7, 7, 10, 3]

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
