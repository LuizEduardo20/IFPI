def contar_letra(alfabeto, letra_busca):
    contador = 0

    for letra in alfabeto:
        if letra == letra_busca:
            contador += 1

    return contador

def main():
    alfabeto = ['A', 'B', 'C', 'A', 'D', 'A', 'E']
    contador_A = contar_letra(alfabeto, 'A')
    assert contador_A == 3
    
    alfabeto = ['B', 'C', 'D', 'E']
    contador_A = contar_letra(alfabeto, 'A')
    assert contador_A == 0

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
