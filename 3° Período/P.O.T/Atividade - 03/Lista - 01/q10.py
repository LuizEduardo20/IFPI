def max(a, b, c, d):
    return max([a, b, c, d])

def main():
    assert max(1, 2, 3, 4) == 4
    assert max(-1, -2, -3, -4) == -1
    assert max(-1, -2, -3, -4) == -1
    assert max(5, 5, 5, 5) == 5
    
    print("Todos os testes de max passaram!")

if __name__ == "__main__":
    main()
