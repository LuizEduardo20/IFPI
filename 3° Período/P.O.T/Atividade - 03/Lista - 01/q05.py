def pesoIdeal(h, s):
    if s == 1:
        return (72.7 * h) - 58
    elif s == 2:
        return (62.1 * h) - 44.7
    return None

def main():
    assert pesoIdeal(1.70, 1) - 65.59 < 0.01
    assert pesoIdeal(1.60, 2) - 54.66 < 0.01
    assert pesoIdeal(1.70, 3) is None
    
    print("Todos os testes de Peso Ideal passaram!")

if __name__ == "__main__":
    main()
