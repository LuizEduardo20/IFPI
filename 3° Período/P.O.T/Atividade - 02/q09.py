X = []

while True:
    try:
        for i in range(5):
            numero = int(input(f"Digite o {i+1}º número: "))
            X.append(numero)
            Y = X[::-1]
            
        print("\nLista X:", X)
        print("Lista Y:", Y)
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos!")
