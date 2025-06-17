def maior_soma_repetidos(lista):
    contagem = {}
    for numero in lista:
        contagem[numero] = contagem.get(numero, 0) + 1
    
    maior_soma = 0
    for numero, quantidade in contagem.items():
        if quantidade > 1:
            soma = numero * quantidade
            if soma > maior_soma:
                maior_soma = soma
    
    return maior_soma

def main():
    assert maior_soma_repetidos([5, -2, -2, 5, 3]) == 10
    assert maior_soma_repetidos([1, 2, 3, 4, 5]) == 0
    assert maior_soma_repetidos([1, 1, 1, 1]) == 4
    assert maior_soma_repetidos([-2, -2, 3, 3]) == 6
    assert maior_soma_repetidos([]) == 0
    assert maior_soma_repetidos([5, 5, 5, 2, 2]) == 15
    print('✅ Testes da função maior_soma_repetidos passaram!')

if __name__ == '__main__':
    main()
