def inverso(lista):
    lista_invertida = []

    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
        
    return lista_invertida

def main():
    lista = [1, 2, 3, 4, 5]
    lista_invertida = inverso(lista)
    assert lista_invertida == [5, 4, 3, 2, 1]
    
    lista = [10, 20, 30]
    lista_invertida = inverso(lista)
    assert lista_invertida == [30, 20, 10]
    
    lista = [1]
    lista_invertida = inverso(lista)
    assert lista_invertida == [1]
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
