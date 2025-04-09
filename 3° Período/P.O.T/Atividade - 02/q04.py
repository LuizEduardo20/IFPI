l = []
cont = 0
maior = 0
menor = 0

def verifica_maior(n, maior, pos_maior, i):
    if n > maior:
        maior = n
        pos_maior = i
    return maior, pos_maior

def verifica_menor(n, menor, pos_menor, i):
    if n < menor:
        menor = n
        pos_menor = i
    return menor, pos_menor

for i in range(5):
    while True:
        try:
            n = int(input('Digite um número: '))
            if cont == 0:
                maior = n
                menor = n
                pos_maior = i
                pos_menor = i
                
            maior, pos_maior = verifica_maior(n, maior, pos_maior, i)
            menor, pos_menor = verifica_menor(n, menor, pos_menor, i)
                    
            cont += 1
            break
        except:
            print('Valor inválido, tente novamente: ')
            
print(f'O número {maior} é o maior número e está na posição {pos_maior} da lista')
print(f'O número {menor} é o menor número e está na posição {pos_menor} da lista')
