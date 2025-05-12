def calcular_pontuacao(gabarito, respostas):
    pontuacao = 0
    
    for i in range(len(gabarito)):
        if respostas[i] == gabarito[i]:
            pontuacao += 1
            
    return pontuacao

def main():
    gabarito = ['A', 'B', 'C', 'D', 'E']
    respostas1 = ['A', 'B', 'C', 'D', 'E']
    respostas2 = ['A', 'B', 'C', 'A', 'B']
    
    assert calcular_pontuacao(gabarito, respostas1) == 5
    assert calcular_pontuacao(gabarito, respostas2) == 3
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
