def somatoria(n):
    if n <= 0:
        return "Por favor, insira um número positivo"
    
    s = 0
    for t in range(1, n + 1):
        s += (t**2 + 1)/(t + 3)
    return s

while True:
    try:
        numero = int(input("Digite um número positivo: "))
        
        resultado = somatoria(numero)
        
        print(f"O valor de S é: {resultado:.2f}")
        
    except ValueError:
        print("Por favor, digite um número válido")
