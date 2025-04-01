def celsius(fahrenheit):
    return ((fahrenheit - 32) / 9) * 5

while True:
    try:
        fahrenheit = float(input('Digita um valor de temperatura: '))
        break
    except:
        print('Valor invalido, Tenta de novo!!')

resultado = celsius(fahrenheit)
print(f'o valor de Fahrenheit {fahrenheit} em Celsius é {resultado:.2f}')
