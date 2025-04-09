def ler_e_modificar_lista():
    lista_C = []
    print("Digite 10 números inteiros:")
    
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista_C.append(numero)
    
    for i in range(len(lista_C)):
        if lista_C[i] < 0:
            lista_C[i] = 0
    
    print(lista_C)

ler_e_modificar_lista()
