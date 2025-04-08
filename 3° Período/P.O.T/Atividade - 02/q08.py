alfabeto = ['A', 'B', 'C', 'A', 'D', 'E', 'A', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A']

contador = 0

for letra in alfabeto:
    while True:
        try:
            if letra == 'A':
                contador += 1
                break
            
        except ValueError:
            print('Erro!! Digite apenas letras')

print(f"Usando um loop, a letra 'A' aparece {contador} vezes na lista.")
