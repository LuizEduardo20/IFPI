def soma_maiores(lista):
    lista_filtrada = []
    
    for x in lista:
        if isinstance(x, int):
            if x >= 0:
                lista_filtrada.append(x)
    
    
    prim_maior = max(lista_filtrada[0], lista_filtrada[1])
    seg_maior = min(lista_filtrada[0], lista_filtrada[1])

    for numero in lista_filtrada[2:]:
        if numero > prim_maior:
            seg_maior = prim_maior
            prim_maior = numero
        elif numero > seg_maior:
            seg_maior = numero

    return prim_maior + seg_maior




def main():
    assert soma_maiores([1, 2, 3, 4, 6]) == 10
    assert soma_maiores([10, 20, -5, "a"]) == 30
    assert soma_maiores([5, 5, "b", -2]) == 10
    assert soma_maiores(["a", "b", 100, 99, -1]) == 199
    assert soma_maiores([0, 0, 5, "z"]) == 5
    print("✅ Todos os testes passaram!")

if __name__ == "__main__":
    main()

