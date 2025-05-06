def area_circulo(r):
    area = 3.14 * r ** 2
    return round(area, 2)

def perimetro_circulo(r):
    perimetro = 3.14 * 2 * r
    return round(perimetro, 2)

def main():
    assert area_circulo(1) == 3.14
    assert area_circulo(2) == 12.56
    assert area_circulo(0) == 0.0
    assert area_circulo(5) == 78.5

    assert perimetro_circulo(1) == 6.28
    assert perimetro_circulo(2) == 12.56
    assert perimetro_circulo(0) == 0.0
    assert perimetro_circulo(5) == 31.4

    print("Todos os testes passaram com sucesso!")

if __name__ == '__main__':
    main()
