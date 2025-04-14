def inserir_numeros():
    X = []
    for i in range(5):
        while True:
            try:
                numero = int(input(f"Digite o {i+1}º número: "))
                X.append(numero)
                break
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos!")
    return X

def inverter_lista(lista):
    return lista[::-1]

X = inserir_numeros()
Y = inverter_lista(X)

print("\nLista X:", X)
print("Lista Y:", Y)
