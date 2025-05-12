def somar(n1, n2):
    return n1 + n2

def main():
    assert somar(2, 3) == 5
    assert somar(-2, -3) == -5
    assert somar(0, 0) == 0
    
    print("Todos os testes de somar passaram!")

if __name__ == "__main__":
    main()
