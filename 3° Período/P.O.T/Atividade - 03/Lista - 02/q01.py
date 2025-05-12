def impa_par(valor):
    listaPar = []
    listaImpar = []

    if valor % 2 == 0:
        listaPar.append(valor)

    else:
        listaImpar.append(valor)

    return listaPar, listaImpar

def main():
    listaPar, listaImpar = impa_par(2)
    assert listaPar == [2]
    assert listaImpar == []
    
    listaPar, listaImpar = impa_par(3)
    assert listaPar == []
    assert listaImpar == [3]
    
    listaPar, listaImpar = impa_par(4)
    assert listaPar == [4]
    assert listaImpar == []
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()