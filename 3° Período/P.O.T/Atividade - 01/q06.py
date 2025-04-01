def poligonos(lf, cm):
    if lf == 3:
        area = (cm * cm * (3 ** 0.5)) / 4
        print(f"Área do triângulo: {area:.2f} cm²")

    elif lf == 4:
        area = cm * cm
        print(f"Área do quadrado: {area:.2f} cm²")

    elif lf == 5:
        area = (5 * cm * cm) / (4 * (5 ** 0.5) ** 0.5)
        print(f"Área do pentágono: {area:.2f} cm²")
    
    else:
        print('Valores Invalidos')

while True:
    try:
        ladosFiguras = int(input('Digite a quantidade de lados da figura(Triangulo(3), Quadrado(4), Pentagono(5)): '))
        if ladosFiguras >= 3 and ladosFiguras <= 5:
            break
        else:
            print('Erro!! Tente Novamente!!')
    except ValueError:
        print('Valor Invalido!!')
while True:
    try:
        cm = float(input('Digite em cm o lado do poligono: '))
        break
    except ValueError:
        print('Valor Invalido!!')

resultado = poligonos(ladosFiguras, cm)
