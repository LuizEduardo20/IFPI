def tem_duplicados(lista):
    if len(lista) < 2:
        return False
    
    elementos_vistos = set()
    
    for numero in lista:
        if numero in elementos_vistos:
            return True
        elementos_vistos.add(numero)
    
    return False

def main():
    assert tem_duplicados([1, 2, 3, 1]) == True 
    assert tem_duplicados([3, 7, 2, 4]) == False
    assert tem_duplicados([1, 1, 1, 1]) == True
    assert tem_duplicados([]) == False
    assert tem_duplicados([1]) == False
    assert tem_duplicados([1, 2, 3, 4, 5, 5]) == True
    assert tem_duplicados([1, 1, 2, 3, 4]) == True
    print('✅ Todos os testes passaram!')

if __name__ == '__main__':
    main()  
