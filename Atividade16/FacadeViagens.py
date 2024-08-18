class SistemaReservaAerea:
    def __init__(self):
        self.preco_assentos = {
            'Economica': 500,
            'Executiva': 500 * 2.5,
            'Primeira Classe': 500 * 2.5 * 1.5
        }
        self.disposicao_assentos = [f"{i + 1}{letra}" for i in range(32) for letra in 'ABCDEF']
    
    def reservar_assento(self, classe, assento):
        if classe not in self.preco_assentos:
            raise ValueError("Tipo de classe inválido.")
        if assento not in self.disposicao_assentos:
            raise ValueError("Assento inválido.")
        return self.preco_assentos[classe]

class SistemaReservaHotel:
    def __init__(self):
        self.preco_quartos = {
            'Simples': 200,
            'Executivo': 200 * 1.5,
            'Suite Presidencial': 200 * 1.5 * 3
        }
    
    def reservar_quarto(self, tipo_quarto, num_pessoas):
        if tipo_quarto not in self.preco_quartos:
            raise ValueError("Tipo de quarto inválido.")
        return self.preco_quartos[tipo_quarto] * num_pessoas

class SistemaAluguelCarro:
    def __init__(self):
        self.preco_carros = {
            'Economico': 150,
            'Executivo': 150 * 2,
            'Luxo': 150 * 2 * 2
        }
    
    def alugar_carro(self, tipo_carro, dias):
        if tipo_carro not in self.preco_carros:
            raise ValueError("Tipo de carro inválido.")
        return self.preco_carros[tipo_carro] * dias

class SistemaPagamento:
    def __init__(self):
        self.metodos_pagamento = {
            'Pix': 0.9,
            'Boleto': 0.95,
            'Debito': 1.0,
            'Credito': 1.0399  
        }
    
    def calcular_pagamento(self, metodo, valor_total, num_parcelas=1):
        if metodo not in self.metodos_pagamento:
            raise ValueError("Metodo de pagamento inválido.")
        if metodo == 'Credito' and num_parcelas > 1:
            return valor_total * (1 + 0.0399 * (num_parcelas - 1))
        return valor_total * self.metodos_pagamento[metodo]

class FacadePacoteViagem:
    def __init__(self):
        self.sistema_aereo = SistemaReservaAerea()
        self.sistema_hotel = SistemaReservaHotel()
        self.sistema_carro = SistemaAluguelCarro()
        self.sistema_pagamento = SistemaPagamento()
    
    def reservar_pacote(self, dados_clientes, classe_assento, assentos, tipo_quarto, num_pessoas, tipo_carro, dias, metodo_pagamento, num_parcelas=1):
        total_assentos = sum(self.sistema_aereo.reservar_assento(classe_assento, assento) for assento in assentos)
        preco_quarto = self.sistema_hotel.reservar_quarto(tipo_quarto, num_pessoas)
        preco_carro = self.sistema_carro.alugar_carro(tipo_carro, dias)
        valor_total = total_assentos + preco_quarto + preco_carro
        valor_final = self.sistema_pagamento.calcular_pagamento(metodo_pagamento, valor_total, num_parcelas)
        
        print("Dados dos Clientes:")
        for cliente in dados_clientes:
            print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}")
        
        print("\nDetalhes da Reserva:")
        print(f"Assentos: {', '.join(assentos)} ({classe_assento})")
        print(f"Quarto do Hotel: {tipo_quarto} ({num_pessoas} pessoas)")
        print(f"Aluguel de Carro: {tipo_carro} ({dias} dias)")
        print(f"Metodo de Pagamento: {metodo_pagamento}")
        print(f"Valor Total: R$ {valor_total:.2f}")
        print(f"Valor Final (com descontos ou acrescimos): R$ {valor_final:.2f}")

def main():
    dados_clientes = [
        {"nome": "Joao Vitor", "cpf": "12345678901"},
        {"nome": "Namorada", "cpf": "12345678902"}
    ]
    
    facade = FacadePacoteViagem()
    facade.reservar_pacote(
        dados_clientes,
        classe_assento='Executiva', #Economica / Executiva/ Primeira Classe
        assentos=['4A', '4B'],  #CASAL 2 assentos diferentes
        tipo_quarto='Executivo', #'Simples / Executivo / Suite Presidencial
        num_pessoas=2,
        tipo_carro='Luxo', #Economico/ Executivo / Luxo
        dias=5,
        metodo_pagamento='Credito', #PIX / BOLETO / CREDITO / DEBITO
        num_parcelas=6
    )

if __name__ == "__main__":
    main()
