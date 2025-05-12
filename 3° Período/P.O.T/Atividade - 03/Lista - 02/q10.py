def encontrar_maior_e_menor(lista):
    maior = lista[0]
    posicao_maior = 0
    menor = lista[0]
    posicao_menor = 0

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao_maior = i

        if lista[i] < menor:
            menor = lista[i]
            posicao_menor = i

    return maior, posicao_maior, menor, posicao_menor

def main():
    lista = [5, 3, 8, 1, 9]
    maior, posicao_maior, menor, posicao_menor = encontrar_maior_e_menor(lista)

    assert maior == 9
    assert posicao_maior == 4
    assert menor == 1
    assert posicao_menor == 3

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
