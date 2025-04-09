def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = float(input(f"Digite o {i+1}º número: "))
        lista.append(numero)
    return lista

def copiar_negativos(lista_original):
    lista_negativos = []
    for numero in lista_original:
        if numero < 0:
            lista_negativos.append(numero)
    return lista_negativos

def exibir_listas(lista_original, lista_negativos):
    print("\nLista original (X):", lista_original)
    print("Lista de negativos (R):", lista_negativos)

def main():
    TAMANHO = 10

    lista_x = ler_lista(TAMANHO)
    lista_r = copiar_negativos(lista_x)
    exibir_listas(lista_x, lista_r)

if __name__ == "__main__":
    main()
