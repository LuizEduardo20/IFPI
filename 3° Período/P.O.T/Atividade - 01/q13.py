def somatorio(n):
    if n <= 0:
        return "Por favor, insira um número positivo"
    
    s = 0
    for i in range(1, n + 1):
        s += 1/i
    return s

while True:
    try:
        numero = int(input("Digite um número positivo: "))
        
        resultado = somatorio(numero)
        
        print(f"O valor de S é: {resultado:.2f}")
        
    except ValueError:
        print("Por favor, digite um número válido")
