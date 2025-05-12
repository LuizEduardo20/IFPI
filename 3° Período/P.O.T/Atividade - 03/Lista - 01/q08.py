def calcular(n):
    return n ** 3

def main():
    assert calcular(2) == 8
    assert calcular(-2) == -8
    assert calcular(0) == 0
    
    print("Todos os testes de calcular passaram!")

if __name__ == "__main__":
    main()