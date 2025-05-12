def criar_lista_y(lista_x):
    Y = []

    for i in range(len(lista_x)):
        if i % 2 == 0:
            Y.append(lista_x[i] / 2)

        else:
            Y.append(lista_x[i] * 3)

    return Y

def main():
    lista_x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    lista_y = criar_lista_y(lista_x)
    
    assert lista_y == [1.0, 12, 3.0, 24, 5.0, 36, 7.0, 48, 9.0, 60]
    assert lista_y == [2.0, 1, 1.0, 4, 5.0, 66, 4.0, 40, 3.0, 90]
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
