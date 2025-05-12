def contar_faces(resultados):
    faces = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for resultado in resultados:
        faces[resultado] += 1

    return faces

def main():
    resultados = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
    faces = contar_faces(resultados)
    
    assert faces[1] == 2
    assert faces[2] == 2
    assert faces[3] == 2
    assert faces[4] == 2
    assert faces[5] == 1
    assert faces[6] == 1
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
