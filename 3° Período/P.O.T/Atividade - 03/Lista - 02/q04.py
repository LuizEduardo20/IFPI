def verifica_maior(n, maior, pos_maior, i):
    if n > maior:
        maior = n
        pos_maior = i
        
    return maior, pos_maior

def verifica_menor(n, menor, pos_menor, i):
    if n < menor:
        menor = n
        pos_menor = i
        
    return menor, pos_menor

def main():
    lista = [5, 3, 8, 1, 9]
    
    maior = lista[0]
    menor = lista[0]
    
    pos_maior = 0
    pos_menor = 0
    
    for i in range(len(lista)):
        maior, pos_maior = verifica_maior(lista[i], maior, pos_maior, i)
        menor, pos_menor = verifica_menor(lista[i], menor, pos_menor, i)
    
    assert maior == 9
    assert pos_maior == 4
    assert menor == 1
    assert pos_menor == 3
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
