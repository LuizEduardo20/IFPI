def contar_ocorrencias(lista):
    contagem = {}
    for item in lista:
        if isinstance(item, int) and item >= 0:
            if item in contagem:
                contagem[item] += 1
            else:
                contagem[item] = 1
    return contagem

def main():
    assert contar_ocorrencias([1, 2, -1, 'a', 2, 1]) == {1: 2, 2: 2}
    assert contar_ocorrencias([10, '10', -10, 10, 20]) == {10: 2, 20: 1}
    assert contar_ocorrencias([0, 0, 'zero']) == {0: 2}
    assert contar_ocorrencias(['a', 'b', -3]) == {}
    assert contar_ocorrencias([]) == {}

    print("✅ Todos os testes passaram!")

if __name__ == "__main__":
    main()