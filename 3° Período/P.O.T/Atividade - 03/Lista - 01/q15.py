def somatoria(n):
    if n <= 0:
        return None
    return sum((t**2 + 1)/(t + 3) for t in range(1, n + 1))

def main():
    assert abs(somatoria(3) - 3.916) < 0.001
    assert somatoria(-1) is None
    assert somatoria(0) is None
    
    print("Todos os testes de somatoria passaram!")

if __name__ == "__main__":
    main()
