import random
from abc import ABC, abstractmethod

class ItemComponent(ABC):
    @abstractmethod
    def get_preco(self):
        pass

    @abstractmethod
    def get_nome(self):
        pass

    def adicionar(self, item):
        pass

    def remover(self, item):
        pass

#FOLHA ITEM INDIVIDUAL
class Item(ItemComponent):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco

    def get_nome(self):
        return self.nome
    

class Caixa(ItemComponent): # O QUE PODE CONTER NAS CAIXAS
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        self.itens.remove(item)

    def get_preco(self):
        total = 0
        for item in self.itens:
            total += item.get_preco()
        return total

    def get_nome(self):
        return self.nome

    def mostrar_conteudo(self):
        print(f"{self.get_nome()} contem:")
        for item in self.itens:
            print(f"- {item.get_nome()}: R$ {item.get_preco():.2f}") 
        print(f"Valor total da {self.get_nome()}: R$ {self.get_preco():.2f}")

itens_disponiveis = {
    "Quadrinhos": 15.00,
    "Chaveiros": 5.00,
    "Bustos": 10.00,
    "Adesivos": 1.00,
    "Posters": 25.00,
    "Camisetas": 25.00,
    "Canetas": 3.00,
    "Miniaturas": 20.00
}

categorias_clientes = {
    "Bronze": 3,
    "Prata": 5,
    "Ouro": 7,
    "Platina": 10
}

def criar_caixa(categoria):
    if categoria not in categorias_clientes:
        raise ValueError("Categoria inválida!")
    
    qtd_itens = categorias_clientes[categoria]
    caixa = Caixa(f"Caixa de assinatura - Categoria {categoria}")
    
    for _ in range(qtd_itens):
        item_nome, item_preco = random.choice(list(itens_disponiveis.items()))
        item = Item(item_nome, item_preco)
        caixa.adicionar(item)
    
    caixa.mostrar_conteudo()

#[[[[[[[[[MUDAR A CATEGORIA DE ACORDO COM O QUE DESEJA]]]]]]]]]]

categoria_cliente = "Platina"  
#categoria_cliente = "Ouro"  
#categoria_cliente = "Prata"
#categoria_cliente = "Bronze"

#[[[[[[[[[MUDAR A CATEGORIA DE ACORDO COM O QUE DESEJA]]]]]]]]]]


criar_caixa(categoria_cliente)
