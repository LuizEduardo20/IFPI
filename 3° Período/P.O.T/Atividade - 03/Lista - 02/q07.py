def verificar_numeros_unicos(lista):
    numeros_unicos = []

    for numero in lista:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)

    return numeros_unicos

def main():
    lista = [1, 2, 3, 2, 4, 5, 1, 6]
    numeros_unicos = verificar_numeros_unicos(lista)
    assert numeros_unicos == [1, 2, 3, 4, 5, 6]
    
    lista = [1, 1, 1, 1]
    numeros_unicos = verificar_numeros_unicos(lista)
    assert numeros_unicos == [1]
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
