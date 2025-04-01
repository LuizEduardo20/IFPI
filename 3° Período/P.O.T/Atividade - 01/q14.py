def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

def somatoria(n):
    if n <= 0:
        return "Por favor, insira um número positivo"
    
    s = 0
    for i in range(n + 1):
        s += 1/fatorial(i)
    return s

while True:
    try:
        numero = int(input("Digite um número positivo: "))
        
        resultado = somatoria(numero)
        
        print(f"O valor de S é: {resultado:.2f}")
        
    except ValueError:
        print("Por favor, digite um número válido")
