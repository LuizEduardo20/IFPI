def ler_gabarito():
    gabarito = []
    for i in range(30):
        while True:
            resposta = input(f"Questão {i+1}: ").upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                gabarito.append(resposta)
                break
            print("Resposta inválida! Digite A, B, C, D ou E.")
    return gabarito

def ler_respostas_aluno(numero_aluno):
    print(f"Respostas do aluno {numero_aluno}:")
    respostas = []
    for i in range(30):
        while True:
            resposta = input(f"Questão {i+1}: ").upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                respostas.append(resposta)
                break
            print("Resposta inválida! Digite A, B, C, D ou E.")
    return respostas

def calcular_pontuacao(gabarito, respostas):
    pontuacao = 0
    for i in range(30):
        if respostas[i] == gabarito[i]:
            pontuacao += 1
    return pontuacao

def main():
    gabarito = ler_gabarito()
    
    while True:
        try:
            num_alunos = int(input("\nDigite o número de alunos: "))
            if num_alunos > 0:
                break
            print("O número de alunos deve ser positivo!")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    for aluno in range(1, num_alunos + 1):
        respostas = ler_respostas_aluno(aluno)
        pontuacao = calcular_pontuacao(gabarito, respostas)
        print(f"Aluno {aluno}: {pontuacao} acertos")

if __name__ == "__main__":
    main()
