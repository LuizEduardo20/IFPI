def remove_repetidos(lista):
    contagem = {}
    for numero in lista:
        contagem[numero] = contagem.get(numero, 0) + 1
    
    return [numero for numero in lista if contagem[numero] == 1]

def main():
    assert remove_repetidos([5, 4, 5, 7, 3, 4]) == [7, 3]
    assert remove_repetidos([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_repetidos([1, 1, 1, 1]) == []
    assert remove_repetidos([]) == []
    assert remove_repetidos([1, 2, 2, 3, 3, 4]) == [1, 4]
    print('✅ Testes da função remove_repetidos passaram!')

if __name__ == '__main__':
    main() 