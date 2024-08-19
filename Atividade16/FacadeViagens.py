class SistemaReservaAerea:
    def __init__(self):
        self.preco_assentos = {
            'Economica': 500,
            'Executiva': 500 * 2.5,
            'Primeira Classe': 500 * 2.5 * 1.5
        }
        self.disposicao_assentos = {
            "A": "Janela",
            "B": "Meio",
            "C": "Corredor",
            "D": "Corredor",
            "E": "Meio",
            "F": "Janela"
        }
        self.fileiras_classes = {
            "Primeira Classe": range(1, 4),
            "Executiva": range(4, 9),
            "Economica": range(9, 33)
        }

    def reservar_assento(self, classe, assento):
        fileira, letra = int(assento[:-1]), assento[-1]
        
        if classe not in self.preco_assentos:
            raise ValueError("Tipo de classe inválido.")
        
        if fileira not in self.fileiras_classes[classe]:
            raise ValueError(f"Assento {assento} não pertence à classe {classe}.")
        
        if letra not in self.disposicao_assentos:
            raise ValueError("Assento inválido.")
        
        return self.preco_assentos[classe], self.disposicao_assentos[letra]

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
    def calcular_pagamento(self, metodo_pagamento, valor_total, num_parcelas=1):
        if metodo_pagamento == 'Pix':
            return valor_total * 0.9
        elif metodo_pagamento == 'Boleto':
            return valor_total * 0.95
        elif metodo_pagamento == 'Debito':
            return valor_total
        elif metodo_pagamento == 'Credito':
            juros = 1.0399 ** (num_parcelas - 1)
            return valor_total * juros
        else:
            raise ValueError("Método de pagamento inválido.")

class FacadePacoteViagem:
    def __init__(self):
        self.sistema_aereo = SistemaReservaAerea()
        self.sistema_hotel = SistemaReservaHotel()
        self.sistema_carro = SistemaAluguelCarro()
        self.sistema_pagamento = SistemaPagamento()
    
    def reservar_pacote(self, dados_clientes, classe_assento, assentos, tipo_quarto, num_pessoas, tipo_carro, dias, metodo_pagamento, num_parcelas=1):
        total_assentos = 0
        detalhes_assentos = []
        for assento in assentos:
            preco_assento, posicao = self.sistema_aereo.reservar_assento(classe_assento, assento)
            total_assentos += preco_assento
            detalhes_assentos.append(f"{assento} ({posicao})")
        
        preco_quarto = self.sistema_hotel.reservar_quarto(tipo_quarto, num_pessoas)
        preco_carro = self.sistema_carro.alugar_carro(tipo_carro, dias)
        valor_total = total_assentos + preco_quarto + preco_carro
        valor_final = self.sistema_pagamento.calcular_pagamento(metodo_pagamento, valor_total, num_parcelas)
        
        print("Dados dos Clientes:")
        for cliente in dados_clientes:
            print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}")
        
        print("\nDetalhes da Reserva:")
        print(f"Assentos: {', '.join(detalhes_assentos)} ({classe_assento})")
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
    #EXEMPLO CRIADO PARA TESTES
    facade = FacadePacoteViagem()
    facade.reservar_pacote(
        dados_clientes,
        classe_assento='Executiva',  #Economica /Executiva /Primeira Classe
        assentos=['4A', '4B'],  
        tipo_quarto='Executivo',  #Simples /Executivo /Suite Presidencial
        num_pessoas=2,  
        tipo_carro='Luxo',  #Economico/ Executivo /Luxo
        dias=5,  
        metodo_pagamento='Credito',  #Pix / Bolet o /Debito /Credito
        num_parcelas=6  
    )

if __name__ == "__main__":
    main()
