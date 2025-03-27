def somarMedia(n1, n2):
  if 6 < (n1 + n2) / 2:
    print('Aprovado')

  else:
    print('Reprovado')

while True:
  try:
    nota1 = float(input('Digite a primeira nota: ')
    nota2 = float(input('Digite a segunda nota: ')
    break

  except ValueError:
    print('Valores Invalidos')

resultado = somarMedia(nota1, nota2)
