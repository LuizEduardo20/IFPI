def encontrar_ocorrencias(lista, valor):
    posicoes = []
    
    for i in range(len(lista)):
        if lista[i] == valor:
            posicoes.append(i)

    return posicoes

def main():
    W = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2]
    posicoes = encontrar_ocorrencias(W, 2)
    
    assert posicoes == [1, 3, 5, 7, 9]
    assert len(posicoes) == 5

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
