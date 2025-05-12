def positivo_negativo(valor):
    listaPositivo = []
    listaNegativa = []

    if valor > 0:
        listaPositivo.append(valor)
        
    elif valor < 0:
        listaNegativa.append(valor)
        
    return listaPositivo, listaNegativa

def main():
    listaPositivo, listaNegativa = positivo_negativo(5)
    assert listaPositivo == [5]
    assert listaNegativa == []
    
    listaPositivo, listaNegativa = positivo_negativo(-3)
    assert listaPositivo == []
    assert listaNegativa == [-3]
    
    listaPositivo, listaNegativa = positivo_negativo(0)
    assert listaPositivo == []
    assert listaNegativa == []
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()