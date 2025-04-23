lista = []

def inserir():
    for i in range(5):
        while True:
            try:
                n = int(input('Digite um número: '))
                if verificar(n):
                    print('Número repetido, digite outro.')
                else:
                    lista.append(n)
                    break
            except ValueError:
                print('Valor errado, digite novamente.')
    return lista

def verificar(x):
    return x in lista

x = inserir()
print('Lista final:', x)
