def calcular_faturamento_total(faturamentos):
    return sum(faturamentos)

def calcular_media_faturamentos(faturamentos):
    return sum(faturamentos) / len(faturamentos)

def contar_abaixo_media(faturamentos, media_faturamentos):
    return sum(1 for i in faturamentos if i < media_faturamentos)

def main():
    faturamentos = [100.0, 200.0, 300.0, 400.0, 500.0]
    faturamento_total = calcular_faturamento_total(faturamentos)
    media_faturamentos = calcular_media_faturamentos(faturamentos)
    abaixo_media = contar_abaixo_media(faturamentos, media_faturamentos)
    
    assert faturamento_total == 1500.0
    assert media_faturamentos == 300.0
    assert abaixo_media == 2

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
