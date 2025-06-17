def soma_cumulativa(lista):
    resultado = []
    soma = 0
    for num in lista:
        soma += num
        resultado.append(soma)
    return resultado

def main():
    assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]
    assert soma_cumulativa([5, -2, 4]) == [5, 3, 7]
    assert soma_cumulativa([]) == []
    assert soma_cumulativa([0, 0, 0]) == [0, 0, 0]
    assert soma_cumulativa([10]) == [10]
    assert soma_cumulativa([-1, -2, -3]) == [-1, -3, -6]
    print("✅ Todos os testes passaram!")

if __name__ == "__main__":
    main()
