def verificar_numero(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def main():
    assert verificar_numero(1) == 'ímpar'
    assert verificar_numero(2) == 'par'
    assert verificar_numero(3) == 'ímpar'
    assert verificar_numero(4) == 'par'
    assert verificar_numero(0) == 'par'
    assert verificar_numero(-1) == 'ímpar'
    assert verificar_numero(-2) == 'par'
    assert verificar_numero(7) == 'ímpar'

    print("Todos os testes passaram com sucesso!")

if __name__ == '__main__':
    main()
