from datetime import datetime
import random
import string
import re

class CartaoEmbarque:
    _assentos_ocupados = {}
    
    def __init__(self, nome_passageiro: str, numero_voo: str, codigo_reserva: str, data_hora_embarque: datetime):
        if not nome_passageiro or not isinstance(nome_passageiro, str):
            raise ValueError("Nome do passageiro inválido")
            
        if not numero_voo or not isinstance(numero_voo, str):
            raise ValueError("Número do voo inválido")
            
        if not re.match("^[A-Za-z0-9]{6}$", codigo_reserva):
            raise ValueError("Código de reserva deve conter exatamente 6 caracteres alfanuméricos")
            
        if not isinstance(data_hora_embarque, datetime):
            raise ValueError("Data e hora devem ser um objeto datetime")
        if data_hora_embarque < datetime.now():
            raise ValueError("Data e hora de embarque não podem ser retroativas")
            
        self._nome_passageiro = nome_passageiro
        self._numero_voo = numero_voo
        self._codigo_reserva = codigo_reserva
        self._data_hora_embarque = data_hora_embarque
        
        self._check_in_realizado = False
        self._assento = None
        
        if numero_voo not in CartaoEmbarque._assentos_ocupados:
            CartaoEmbarque._assentos_ocupados[numero_voo] = set()
    
    def nome_passageiro(self):
        return self._nome_passageiro
        
    def numero_voo(self):
        return self._numero_voo
        
    def codigo_reserva(self):
        return self._codigo_reserva
        
    def data_hora_embarque(self):
        return self._data_hora_embarque
        
    def check_in_realizado(self):
        return self._check_in_realizado
        
    def assento(self):
        return self._assento
    
    def _gerar_assento_aleatorio(self):
        while True:
            fileira = random.randint(1, 30)
            letra = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
            assento = f"{fileira}{letra}"
            if assento not in CartaoEmbarque._assentos_ocupados[self._numero_voo]:
                return assento
    
    def realizar_check_in(self):
        if self._check_in_realizado:
            raise ValueError("Check-in já foi realizado")
            
        if datetime.now() > self._data_hora_embarque:
            raise ValueError("Não é possível realizar check-in após o horário do voo")
            
        self._assento = self._gerar_assento_aleatorio()
        CartaoEmbarque._assentos_ocupados[self._numero_voo].add(self._assento)
        self._check_in_realizado = True
        return self._assento
    
    def alterar_assento(self, novo_assento: str):
        if not self._check_in_realizado:
            raise ValueError("É necessário realizar o check-in antes de alterar o assento")
            
        if not re.match("^[1-9][0-9]?[A-F]$", novo_assento):
            raise ValueError("Formato de assento inválido. Use o formato: número da fileira (1-30) + letra (A-F)")
            
        if novo_assento in CartaoEmbarque._assentos_ocupados[self._numero_voo]:
            raise ValueError("Assento já está ocupado")
            
        CartaoEmbarque._assentos_ocupados[self._numero_voo].remove(self._assento)
        CartaoEmbarque._assentos_ocupados[self._numero_voo].add(novo_assento)

        self._assento = novo_assento
        return self._assento
    
    def __str__(self):
        status = "Realizado" if self._check_in_realizado else "Não realizado"
        assento_info = f", Assento: {self._assento}" if self._assento else ""
        return (f"Cartão de Embarque:\n"
                f"Passageiro: {self._nome_passageiro}\n"
                f"Voo: {self._numero_voo}\n"
                f"Localizador: {self._codigo_reserva}\n"
                f"Data/Hora: {self._data_hora_embarque.strftime('%d/%m/%Y %H:%M')}\n"
                f"Check-in: {status}{assento_info}")

if __name__ == "__main__":
    data_voo1 = datetime(2024, 12, 25, 10, 30)
    data_voo2 = datetime(2024, 12, 26, 15, 45)
    data_voo3 = datetime(2024, 12, 27, 8, 20)
    
    try:
        cartao1 = CartaoEmbarque(
            "João Silva",
            "JJ1234",
            "ABC123",
            data_voo1
        )
        
        cartao2 = CartaoEmbarque(
            "Maria Santos",
            "JJ1234",
            "XYZ789",
            data_voo1
        )
        
        cartao3 = CartaoEmbarque(
            "Pedro Oliveira",
            "JJ5678",
            "DEF456",
            data_voo2
        )
        
        print("\nTeste 1: Realizando check-in")
        print(cartao1)
        assento1 = cartao1.realizar_check_in()
        print(f"\nApós check-in:")
        print(cartao1)
        
        print("\nTeste 2: Tentativa de check-in duplicado")
        try:
            cartao1.realizar_check_in()
        except ValueError as e:
            print(f"Erro esperado: {e}")
        
        print("\nTeste 3: Alteração de assento")
        novo_assento = "15A"
        print(f"Tentando alterar para assento {novo_assento}")
        cartao1.alterar_assento(novo_assento)
        print(cartao1)
        
        print("\nTeste 4: Check-in segundo passageiro mesmo voo")
        assento2 = cartao2.realizar_check_in()
        print(cartao2)
        
        print("\nTeste 5: Tentativa de alterar para assento ocupado")
        try:
            cartao2.alterar_assento(novo_assento)
        except ValueError as e:
            print(f"Erro esperado: {e}")
            
    except ValueError as e:
        print(f"Erro na criação ou manipulação dos cartões: {e}")
