def pesoIdeal(h, s):
    if s == 1:
        calculo = (72.7 * h) - 58
        print(f'Seu peso ideal é: {calculo:.2f}')
    
    elif s == 2:
        calculo = (62.1 * h) - 44.7
        print(f'Seu peso ideal é: {calculo:.2f}')
    
    else:
        print('Sexo Invalido!!')

while True:
    try:
        altura = float(input('Digite sua altura: '))
        sexo = float(input('Digite seu sexo (1 - Homem, 2 - Mulher): '))
        break

    except ValueError:
        print('Valores Invalidos!!')

resultado = pesoIdeal(altura, sexo)
