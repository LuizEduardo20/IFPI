def maior_soma_segmento(lista):
    if not lista:
        return 0
    max_atual = max_total = lista[0]
    for num in lista[1:]:
        max_atual = max(num, max_atual + num)
        max_total = max(max_total, max_atual)
    return max_total

def main():
    assert maior_soma_segmento([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34
    assert maior_soma_segmento([-5, -2, -1, -7]) == -1
    assert maior_soma_segmento([1, 2, 3, 4]) == 10
    assert maior_soma_segmento([]) == 0
    assert maior_soma_segmento([7]) == 7
    assert maior_soma_segmento([-7]) == -7
    assert maior_soma_segmento([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("✅ Todos os testes passaram!")

if __name__ == "__main__":
    main()
