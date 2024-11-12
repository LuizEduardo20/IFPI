def valores_matriz(n=4, m=6):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz

def maior_venda(ano, matriz):   
    anos = [2013, 2014, 2015, 2016, 2017, 2018]
    
    for i in range(len(anos)):
        if ano == anos[i]:
            maior = matriz[0][0]
            for j in range(len(matriz)):
                if matriz[j][i] > maior:
                    maior = matriz[j][i]
        return maior
    
def main():
    ano = int(input())
    matriz = valores_matriz()
    maiorVenda = maior_venda(ano, matriz)
    
    print(maiorVenda)
    
if __name__ == "__main__":
    main()
