def cadastrar_nome(lista):
    nome = input("Digite o nome a ser cadastrado: ")
    lista.append(nome)
    print(f"Nome '{nome}' cadastrado com sucesso!")

def pesquisar_nome(lista):
    nome = input("Digite o nome a ser pesquisado: ")
    if nome in lista:
        print(f"O nome '{nome}' foi encontrado na posição {lista.index(nome)}")
    else:
        print(f"O nome '{nome}' não foi encontrado na lista.")

def listar_nomes(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        print("\nLista de nomes:")
        for i, nome in enumerate(lista):
            print(f"{i+1}. {nome}")

def main():
    tamanho = int(input("Digite o número de posições da lista: "))
    lista_nomes = []
    
    while True:
        print("\n==== MENU ====")
        print("1) Cadastrar nome")
        print("2) Pesquisar nome")
        print("3) Listar todos os nomes")
        print("4) Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            if len(lista_nomes) < tamanho:
                cadastrar_nome(lista_nomes)
            else:
                print("A lista está cheia!")
        elif opcao == "2":
            pesquisar_nome(lista_nomes)
        elif opcao == "3":
            listar_nomes(lista_nomes)
        elif opcao == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
