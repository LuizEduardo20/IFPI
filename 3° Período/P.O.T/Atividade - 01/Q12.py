def somatorio(n):
    if n <= 0:
        print("Por favor, insira um número positivo")
    
    soma = 0
    
    for i in range(1, n + 1):
        soma += i
    return soma

while True:
    try:
        numero = int(input("Digite um número positivo (ou 0 para sair): "))
        if numero == 0:
            print("Programa encerrado!")
            break
        resultado = somatorio(numero)
        
        print(f"O somatório de 1 até {numero} é: {resultado}")
        
    except ValueError:
        print("Por favor, digite um número válido")
