def somatorio(n):
    if n <= 0:
        return None
    return sum(1/i for i in range(1, n + 1))

def main():
    assert abs(somatorio(3) - 1.833) < 0.001
    assert somatorio(-1) is None
    assert somatorio(0) is None
    
    print("Todos os testes de somatorio passaram!")

if __name__ == "__main__":
    main()