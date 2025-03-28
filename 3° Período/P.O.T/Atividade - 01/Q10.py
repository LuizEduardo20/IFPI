def Max(a, b, c, d):
    return max(a, b, c, d)

for i in range(4):
    print(f"Série {i + 1}:")
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = int(input("Digite o terceiro número: "))
        d = int(input("Digite o quarto número: "))
        
        maior = Max(a, b, c, d)
        print(f"O maior número é: {maior}")
    except ValueError:
        print("Erro! Digite apenas números inteiros")
