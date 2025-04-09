def ler_lista_x():
    X = []
    for i in range(10):
        while True:
            try:
                numero = int(input(f"Digite o {i+1}º número: "))
                if numero > 0:
                    X.append(numero)
                    break
                else:
                    print("Por favor, digite um número positivo.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
    return X

def criar_lista_y(lista_x):
    Y = []
    for i in range(10):
        if i % 2 == 0:
            Y.append(lista_x[i] / 2)
        else:
            Y.append(lista_x[i] * 3)
    return Y

def exibir_listas(lista_x, lista_y):
    print("\nLista X:", lista_x)
    print("Lista Y:", lista_y)

def main():
    lista_x = ler_lista_x()
    
    lista_y = criar_lista_y(lista_x)
    
    exibir_listas(lista_x, lista_y)

if __name__ == "__main__":
    main()
