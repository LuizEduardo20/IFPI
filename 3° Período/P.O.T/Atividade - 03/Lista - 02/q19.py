def combinar_listas(lista_r, lista_s):
    lista_x = lista_r + lista_s
    
    return lista_x

def main():
    lista_r = [1, 2, 3, 4, 5]
    lista_s = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    lista_x = combinar_listas(lista_r, lista_s)
    
    assert lista_x == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert len(lista_x) == len(lista_r) + len(lista_s)

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
