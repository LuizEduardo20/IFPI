def inverter_lista(lista):
    return lista[::-1]

def main():
    X = [1, 2, 3, 4, 5]
    Y = inverter_lista(X)
    assert Y == [5, 4, 3, 2, 1]
    
    X = [10, 20, 30]
    Y = inverter_lista(X)
    assert Y == [30, 20, 10]
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
