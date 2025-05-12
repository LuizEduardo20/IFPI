def fatorial(n):
    if n == 0 or n == 1:
        return 1
    
    elif n > 0:
        return n * fatorial(n - 1)
    
    else:
        print('Valor inválido!!')

def main():
    assert fatorial(0) == 1
    assert fatorial(5) == 120
    assert fatorial(1) == 1
    assert fatorial(-1) is None
    
    print("Todos os testes de fatorial passaram!")

if __name__ == "__main__":
    main()
