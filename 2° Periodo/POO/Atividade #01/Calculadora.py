class Calculadora():
    valor1 = 0
    valor2 = 0
    operacao = None
    resultado = None

    def calculad(self, valor1, valor2, operacao):
        if operacao == '+':
            self.resultado = valor1 + valor2
            return self.resultado
        
        elif operacao == '-':
            self.resultado = valor1 - valor2
            return self.resultado
        
        elif operacao == '*':
            self.resultado = valor1 * valor2
            return self.resultado
        
        elif operacao == '/':
            self.resultado = valor1 / valor2
            return self.resultado
        
        else:
            print('Operação Invalida')

def main():
    calcular = Calculadora()
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    operacao = input('Digite a operação: [+, -, *, /]').lower()
    print(f' {valor1} {operacao} {valor2} = {calcular.calculad(valor1, valor2, operacao)}')

if __name__ == '__main__':
    main()
