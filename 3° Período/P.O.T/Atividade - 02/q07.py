def inserir_numeros_na_lista():
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
    return lista

lista = inserir_numeros_na_lista()

print(lista)
