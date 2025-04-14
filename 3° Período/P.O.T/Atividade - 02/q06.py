def inserir_dados_produtos():
    faturamentos = []
    for i in range(20):
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade do produto {i+1}: "))
                preco = float(input(f"Digite o preço do produto {i+1}: "))

                faturamento = quantidade * preco
                faturamentos.append(faturamento)

                print(f"Produto {i+1}: Quantidade = {quantidade}, Preço = R$ {preco:.2f}, Faturamento = R$ {faturamento:.2f}")
                break

            except ValueError:
                print('Erro!! Digite apenas números inteiros')
    return faturamentos

def calcular_faturamento_total(faturamentos):
    return sum(faturamentos)

def calcular_media_faturamentos(faturamentos):
    return sum(faturamentos) / len(faturamentos)

def contar_abaixo_media(faturamentos, media_faturamentos):
    return sum(1 for f in faturamentos if f < media_faturamentos)

faturamentos = inserir_dados_produtos()

faturamento_total = calcular_faturamento_total(faturamentos)
media_faturamentos = calcular_media_faturamentos(faturamentos)
abaixo_media = contar_abaixo_media(faturamentos, media_faturamentos)

print("\nResultados:")
print(f"Faturamento Total: R$ {faturamento_total:.2f}")
print(f"Média dos Faturamentos: R$ {media_faturamentos:.2f}")
print(f"Quantidade de produtos com faturamento abaixo da média: {abaixo_media}")
