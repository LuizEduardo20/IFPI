def contar_faces(n):
    faces = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    print(f"Digite os {n} resultados dos lançamentos (um por linha):")
    for i in range(n):
        while True:
            try:
                resultado = int(input())
                if 1 <= resultado <= 6:
                    faces[resultado] += 1
                    break
                else:
                    print("Por favor, digite um número entre 1 e 6.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    for face, contagem in faces.items():
        print(f"Face {face}: {contagem} ocorrências")

while True:
    try:
        n = int(input("Digite o número de lançamentos: "))
        if n > 0:
            break
        else:
            print("Por favor, digite um número positivo.")
    except ValueError:
        print("Por favor, digite um número válido.")

contar_faces(n)
