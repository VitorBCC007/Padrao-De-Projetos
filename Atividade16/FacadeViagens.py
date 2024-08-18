class ReservaPassagem:
    def __init__(self):
        self.classes = {
            'Economica': 500,
            'Executiva': 500 * 2.5,
            'Primeira Classe': 500 * 2.5 * 1.5
        }

    def reservar_assento(self, fileira, poltrona, classe):
        preco = self.classes[classe]
        return f"Assento {fileira}{poltrona} reservado na classe {classe}. Preco: R${preco:.2f}"

class ReservaHotel:
    def __init__(self):
        self.tipos_quarto = {
            'Simples': 200,
            'Executivo': 200 * 1.5,
            'Suite Presidencial': 200 * 1.5 * 3
        }

    def reservar_quarto(self, tipo_quarto, num_pessoas):
        preco = self.tipos_quarto[tipo_quarto] * num_pessoas
        return f"Quarto {tipo_quarto} reservado para {num_pessoas} pessoas. Preco: R${preco:.2f}"

class AluguelCarro:
    def __init__(self):
        self.tipos_carro = { 
            'Economico': 150,
            'Executivo': 150 * 2,  
            'Luxo': 150 * 2 * 2
        }

    def alugar_carro(self, tipo_carro, dias):
        preco = self.tipos_carro[tipo_carro] * dias
        return f"Carro {tipo_carro} alugado por {dias} dias. Preco: R${preco:.2f}"

class Pagamento:
    def calcular_valor_final(self, valor_total, forma_pagamento, parcelas=1):
        descontos = {
            'Pix': 0.1,
            'Boleto': 0.05,
            'Debito': 0,
            'Credito': 0
        }
        acrescimo_credito = 0.0399
        desconto = descontos.get(forma_pagamento, 0)
        valor_com_desconto = valor_total * (1 - desconto)

        if forma_pagamento == 'Credito' and parcelas > 1:
            valor_com_juros = valor_com_desconto * ((1 + acrescimo_credito) ** (parcelas - 1))
            return valor_com_juros, valor_com_juros - valor_total
        return valor_com_desconto, valor_total - valor_com_desconto

class FacadeSistemaViagem:
    def __init__(self):
        self.reserva_passagem = ReservaPassagem()
        self.reserva_hotel = ReservaHotel()
        self.aluguel_carro = AluguelCarro()
        self.pagamento = Pagamento()

    def comprar_pacote(self, nome, cpf, fileira, poltrona, classe_voo, tipo_quarto, num_pessoas, tipo_carro, dias_carro, forma_pagamento, parcelas=1):
        passagem = self.reserva_passagem.reservar_assento(fileira, poltrona, classe_voo)
        hotel = self.reserva_hotel.reservar_quarto(tipo_quarto, num_pessoas)
        carro = self.aluguel_carro.alugar_carro(tipo_carro, dias_carro)

        valor_total = sum([self.reserva_passagem.classes[classe_voo],
                           self.reserva_hotel.tipos_quarto[tipo_quarto] * num_pessoas,
                           self.aluguel_carro.tipos_carro[tipo_carro] * dias_carro])

        valor_final, diferenca = self.pagamento.calcular_valor_final(valor_total, forma_pagamento, parcelas)

        resumo = (
            f"Comprador: {nome}, CPF: {cpf}\n"
            f"{passagem}\n"
            f"{hotel}\n"
            f"{carro}\n"
            f"Forma de pagamento: {forma_pagamento} {'em ' + str(parcelas) + ' parcelas' if parcelas > 1 else ''}\n"
            f"Valor Total do Pacote: R${valor_total:.2f}\n"
            f"Valor Final com Desconto/Juros: R${valor_final:.2f}\n"
            f"Valor {('Desconto' if diferenca >= 0 else 'Acrescimo')}: R${abs(diferenca):.2f}\n"
        )
        
        print(resumo)
        return resumo
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

sistema_viagem = FacadeSistemaViagem()
sistema_viagem.comprar_pacote(
    nome="Joao Vitor",
    cpf="123.456.789-00", 
    fileira=5,
    poltrona="C",
    classe_voo="Executiva", #ALTERAR Executiva / Economica /Primeira Classe
    tipo_quarto="Executivo", #ALTERAR Simples / Executivo / Suite Presidencial
    num_pessoas=2,
    tipo_carro="Luxo", #ALTERAR Economico / Executivo / Luxo
    dias_carro=5,
    forma_pagamento="Credito",#ALTERAR Pix / Boleto / Debito / Credito
    parcelas=3
)


sistema_viagem.comprar_pacote(
    nome="Eduardo ",
    cpf="123.456.789-01", 
    fileira=12,
    poltrona="B",
    classe_voo="Economica", #ALTERAR Executiva / Economica / Primeira Classe
    tipo_quarto="Simples", #ALTERAR Simples / Executivo / Suite Presidencial
    num_pessoas=1,
    tipo_carro="Economico",# ALTERAR Economico / Executivo / Luxo
    dias_carro=3,
    forma_pagamento="Pix" #ALTERAR Pix / Boleto / Debito / Credito
)

sistema_viagem.comprar_pacote(
    nome="Pablo Escobar",
    cpf="123.456.789-02", 
    fileira=1,
    poltrona="A",
    classe_voo="Primeira Classe", # ALTERAR Executiva / Economica / Primeira Classe
    tipo_quarto="Suite Presidencial", # ALTERAR Simples / Executivo / Suite Presidencial
    num_pessoas=4,
    tipo_carro="Luxo", # ALTERAR Economico / Executivo / Luxo
    dias_carro=10,
    forma_pagamento="Credito", # ALTERAR Pix / Boleto / Debito / Credito
    parcelas=12 # Máximo de parcelas para o maior acréscimo
)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
