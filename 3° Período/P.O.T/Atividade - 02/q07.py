lista = []

for i in range(10):
    while True:
        try:
            numeros = int(input(f"Digite o {i+1}º número: "))

            if numeros in lista:
                print('Número já existe na lista')
                
            else:
                lista.append(numeros)
                break

        except ValueError:
            print('Erro!! Digite apenas números inteiros')

print(lista)
