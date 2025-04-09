def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = float(input(f"Digite o {i+1}º elemento da lista: "))
        lista.append(numero)
    return lista

def contar_ocorrencias(lista, valor):
    return lista.count(valor)

def encontrar_posicoes(lista, valor):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == valor:
            posicoes.append(i)
    return posicoes

def main():
    W = ler_lista(10)
    
    V = float(input("\nDigite o valor V para buscar na lista: "))
    
    ocorrencias = contar_ocorrencias(W, V)
    
    posicoes = encontrar_posicoes(W, V)
    
    print(f"\nO valor {V} aparece {ocorrencias} vez(es) na lista.")
    if ocorrencias > 0:
        print(f"O valor {V} aparece nas seguintes posições: {posicoes}")

if __name__ == "__main__":
    main()
