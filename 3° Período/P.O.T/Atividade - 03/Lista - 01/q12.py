def somatorio(n):
    if n <= 0:
        return None
    return sum(range(1, n + 1))

def main():
    assert somatorio(5) == 15
    assert somatorio(-1) is None
    assert somatorio(0) is None
    
    print("Todos os testes de somatorio passaram!")

if __name__ == "__main__":
    main()
