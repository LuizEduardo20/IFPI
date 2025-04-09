def ler_lista(tamanho, nome_lista):
    lista = []
    print(f"\nDigite os {tamanho} elementos da lista {nome_lista}:")
    for i in range(tamanho):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        lista.append(elemento)
    return lista

def combinar_listas(lista_r, lista_s):
    lista_x = lista_r + lista_s
    return lista_x

def exibir_lista(lista, nome_lista):
    print(f"\nLista {nome_lista}:")
    for i, elemento in enumerate(lista):
        print(f"Posição {i}: {elemento}")

def main():
    lista_r = ler_lista(5, "R")
    lista_s = ler_lista(10, "S")
    lista_x = combinar_listas(lista_r, lista_s)
    
    exibir_lista(lista_r, "R")
    exibir_lista(lista_s, "S")
    exibir_lista(lista_x, "X")

if __name__ == "__main__":
    main()
