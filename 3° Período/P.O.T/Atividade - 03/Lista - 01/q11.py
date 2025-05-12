def divisores(n):
    if n <= 0:
        return None
    return len([i for i in range(1, n + 1) if n % i == 0])

def main():
    assert divisores(7) == 2
    assert divisores(12) == 6
    assert divisores(12) == 6
    assert divisores(-1) is None
    
    print("Todos os testes de divisores passaram!")

if __name__ == "__main__":
    main()
