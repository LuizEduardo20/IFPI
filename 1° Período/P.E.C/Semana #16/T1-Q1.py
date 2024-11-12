def ler_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = float(input())
            linha.append(valor) 
        matriz.append(linha)
    return matriz

def comparar_maior(matriz):
    maior = matriz[0][0]
    posicao_maior = (0,0)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                posicao_maior = (i, j)
    return posicao_maior  
 
def comparar_menor(matriz):
    menor = matriz[0][0]
    posicao_menor = (0,0)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                posicao_menor = (i, j)
    return posicao_menor   

def main():
    n = int(input())   
    matriz = ler_matriz(n)
    tupla_indices_maior = comparar_maior(matriz)
    tupla_indices_menor = comparar_menor(matriz)

    print(tupla_indices_maior)
    print(tupla_indices_menor)
    
if __name__ == "__main__":
    main()
