def ler_lista():
    lista = []
    for i in range(10):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        lista.append(elemento)
    return lista

def criar_lista_inversa(lista_original):
    return lista_original[::-1]

def exibir_listas(lista_original, lista_inversa):
    print("Lista D (original):")
    print(lista_original)
    print("Lista E (inversa):")
    print(lista_inversa)

def main():
    D = ler_lista()
    E = criar_lista_inversa(D)
    exibir_listas(D, E)

if __name__ == "__main__":
    main()
