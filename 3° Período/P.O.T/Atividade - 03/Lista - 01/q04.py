def somarMedia(n1, n2):
    media = (n1 + n2) / 2
    if media > 6:
        return 'Aprovado'
    return 'Reprovado'

def main():
    assert somarMedia(7, 8) == 'Aprovado'
    assert somarMedia(5, 5) == 'Reprovado'
    assert somarMedia(6, 6) == 'Reprovado'
    
    print("Todos os testes de somarMedia passaram!")

if __name__ == "__main__":
    main()