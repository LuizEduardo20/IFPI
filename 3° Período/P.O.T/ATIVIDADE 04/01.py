def eliminar_repeticoes(lista=None):
    if lista is None:
        return None

    elementos_unicos_inteiros_positivos = []
    for item in lista:
        if isinstance(item, int):
            valor_absoluto = abs(item)
            if valor_absoluto not in elementos_unicos_inteiros_positivos:
                elementos_unicos_inteiros_positivos.append(valor_absoluto)
            
    return elementos_unicos_inteiros_positivos

def main():
    assert eliminar_repeticoes([1, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert eliminar_repeticoes([-1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert eliminar_repeticoes(['a', -4, 4, 'b', 5, 'a', 6, 4.5]) == [4, 5, 6]
    assert eliminar_repeticoes(['a', 4, 5, 6]) == [4, 5, 6]
    assert eliminar_repeticoes([1, -1, -2, 2, 3, -1, 3]) == [1, 2, 3]
    assert eliminar_repeticoes(['a', 'b', 'c', 3.14]) == []
    assert eliminar_repeticoes([1, 2.5, -3, 4.0, 5, -1]) == [1, 3, 5]

    print("✅ Todos os testes passaram!")

if __name__ == "__main__":
    main()
