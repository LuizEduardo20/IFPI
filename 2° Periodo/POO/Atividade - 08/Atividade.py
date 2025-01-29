class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self._numero = numero
        self._saldo = saldo
    
    def __str__(self):
        return f"Conta: {self._numero} - Saldo: R$ {self._saldo:.2f}"
    
    def creditar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    def debitar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
    
    def transferir(self, valor, conta_destino):
        if self.debitar(valor):
            if conta_destino.creditar(valor):
                return True
        return False
    
    @property
    def saldo(self):
        return self._saldo


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, taxa_juros, saldo=0):
        super().__init__(numero, saldo)
        self._taxa_juros = taxa_juros
    
    def __str__(self):
        return super().__str__() + f" - Taxa de Juros: {self._taxa_juros}%"
    
    def render_juros(self):
        juros = self._saldo * (self._taxa_juros / 100)
        self.creditar(juros)


class ContaImposto(ContaCorrente):
    def __init__(self, numero, percentual_imposto, saldo=0):
        super().__init__(numero, saldo)
        self._percentual_imposto = percentual_imposto
    
    def __str__(self):
        return super().__str__() + f" - Percentual de Imposto: {self._percentual_imposto}%"
    
    def calcula_imposto(self):
        imposto = self._saldo * (self._percentual_imposto / 100)
        self.debitar(imposto)

conta1 = ContaCorrente(1, 1000)
conta2 = ContaPoupanca(2, 5, 500)
conta3 = ContaImposto(3, 10, 2000)

print(conta1)
conta1.transferir(200, conta2)
conta2.render_juros()
conta3.calcula_imposto()
