def poligonos(lf, cm):
    if lf == 3:
        return (cm * cm * (3 ** 0.5)) / 4
    elif lf == 4:
        return cm * cm
    elif lf == 5:
        return (5 * cm * cm) / (4 * (5 ** 0.5) ** 0.5)
    return None

def main():
    assert poligonos(3, 2) - 1.732 < 0.001
    assert poligonos(4, 2) == 4
    assert poligonos(4, 2) == 4
    assert poligonos(6, 2) is None
    
    print("Todos os testes de poligonos passaram!")

if __name__ == "__main__":
    main()
