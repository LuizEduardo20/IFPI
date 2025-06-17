def ordenada(lista):
    lista_limpa = []

    for numero in lista:
        if isinstance(numero, int) and numero >= 0:
            lista_limpa.append(numero)

    if len(lista_limpa) < 2:
        return None

    for i in range(len(lista_limpa) - 1):
        if lista_limpa[i] > lista_limpa[i + 1]:
            return False
    return True


def main():
    assert ordenada([1,2,3,4]) == True
    assert ordenada([6,4,3]) == False
    assert ordenada([-1,2,3,4]) == True
    assert ordenada([-1,3,4,7]) == True
    assert ordenada(['um',2,3,4]) == True
    assert ordenada([3,'dois', 1]) == False
    assert ordenada([-3,'dois', 2]) is None 
    print('✅ Todos os testes passaram!')
if __name__ == '__main__':
    main()