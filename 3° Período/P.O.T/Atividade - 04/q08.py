def valor_mais_proximo_media(lista):
    if not lista:
        return None
    
    media = sum(lista) / len(lista)
    valor_mais_proximo = lista[0]
    menor_diferenca = abs(lista[0] - media)
    
    for numero in lista[1:]:
        diferenca = abs(numero - media)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            valor_mais_proximo = numero
    
    return valor_mais_proximo

def main():
    assert valor_mais_proximo_media([2.5, 7.5, 10.0, 4.0]) == 7.5
    assert valor_mais_proximo_media([1, 2, 3, 4, 5]) == 3
    assert valor_mais_proximo_media([10, 20, 30]) == 20
    assert valor_mais_proximo_media([1, 1, 1, 1]) == 1
    assert valor_mais_proximo_media([]) is None
    print('✅ Testes da função valor_mais_proximo_media passaram!')

if __name__ == '__main__':
    main()
