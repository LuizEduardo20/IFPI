def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

def somatoria(n):
    if n <= 0:
        return None
    return sum(1/fatorial(i) for i in range(n + 1))

def main():
    assert abs(somatoria(3) - 2.666) < 0.001
    assert somatoria(-1) is None
    assert somatoria(0) == 1
    
    print("Todos os testes de somatoria passaram!")

if __name__ == "__main__":
    main()
