def copiar_negativos(lista_original):
    lista_negativos = []

    for numero in lista_original:
        if numero < 0:
            lista_negativos.append(numero)

    return lista_negativos

def main():
    lista_x = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    lista_r = copiar_negativos(lista_x)
    
    assert lista_r == [-2, -4, -6, -8, -10]
    assert lista_x == [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
