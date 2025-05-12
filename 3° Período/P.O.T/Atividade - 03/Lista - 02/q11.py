def cadastrar_nome(lista, nome):
    lista.append(nome)
    
    return lista

def pesquisar_nome(lista, nome):
    if nome in lista:
        return lista.index(nome)
        
    return -1

def listar_nomes(lista):
    if not lista:
        print("A lista está vazia.")

    else:
        for i, nome in enumerate(lista):
            print(f"{i+1}. {nome}")

def main():
    lista_nomes = []
    lista_nomes = cadastrar_nome(lista_nomes, "João")
    lista_nomes = cadastrar_nome(lista_nomes, "Maria")
    lista_nomes = cadastrar_nome(lista_nomes, "Pedro")
    
    assert lista_nomes == ["João", "Maria", "Pedro"]
    assert pesquisar_nome(lista_nomes, "Maria") == 1
    assert pesquisar_nome(lista_nomes, "Ana") == -1

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
