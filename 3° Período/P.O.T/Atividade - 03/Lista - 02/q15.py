def criar_lista_inversa(lista_original):
    return lista_original[::-1]

def main():
    D = [1, 2, 3, 4, 5]
    E = criar_lista_inversa(D)
    
    assert E == [5, 4, 3, 2, 1]
    assert D == [1, 2, 3, 4, 5]

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
