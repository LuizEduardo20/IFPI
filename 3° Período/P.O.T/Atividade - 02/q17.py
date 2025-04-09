def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = int(input(f"Digite o {i+1}º elemento da lista: "))
        lista.append(numero)
    return lista

def encontrar_ocorrencias(lista, valor):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == valor:
            posicoes.append(i)
    return posicoes

def main():
    W = ler_lista(10)
    
    V = int(input("\nDigite o valor V para buscar na lista: "))
    
    posicoes = encontrar_ocorrencias(W, V)
    
    if len(posicoes) == 0:
        print(f"\nO valor {V} não ocorre nenhuma vez na lista W.")
    else:
        print(f"\nO valor {V} ocorre {len(posicoes)} vez(es) na lista W.")
        print(f"O valor {V} aparece nas seguintes posições: {posicoes}")

if __name__ == "__main__":
    main()
