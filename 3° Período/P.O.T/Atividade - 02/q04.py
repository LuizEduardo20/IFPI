l = []
cont = 0
maior = 0
menor = 0



for i in range(5):
    while True:
        try:
            n = int(input('Digite um número: '))
            if cont == 0:
                maior = n
                menor = n
                pos_maior = i
                pos_menor = i
                
            if n > maior:
                maior = n
                pos_maior = i
                
            if n < menor:
                menor = n
                pos_menor = i
                    
            cont += 1
            break
        except:
            print('Valor inválido, tente novamente: ')
            
            
print(f'O número {maior} é o maior número e está na posição {pos_maior} da lista')
print(f'O número {menor} é o menor número e está na posição {pos_menor} da lista')
