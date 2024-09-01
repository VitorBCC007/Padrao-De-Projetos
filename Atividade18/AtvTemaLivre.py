# Importa bibliotecas para criar interfaces e classes abstratas
from abc import ABC, abstractmethod

# Interface de Pedido
class Pedido(ABC):
    @abstractmethod
    def processar_pedido(self) -> str:
        pass

# Classe Pedido Normal
class PedidoNormal(Pedido):
    def __init__(self, id: int, detalhes: str):
        self.id = id
        self.detalhes = detalhes

    def processar_pedido(self) -> str:
        return f"Processando o pedido {self.id} com os detalhes: {self.detalhes}"

# Classe Decorador Base
class PedidoDecorador(Pedido):
    def __init__(self, pedido: Pedido):
        self.pedido = pedido

    def processar_pedido(self) -> str:
        return self.pedido.processar_pedido()

# Decorador Concreto - Embrulho para Presente
class PedidoComEmbrulho(PedidoDecorador):
    def processar_pedido(self) -> str:
        # Adiciona o embrulho para presente ao pedido
        return self.pedido.processar_pedido() + " + com embrulho para presente"

# Decorador Concreto - Seguro
class PedidoComSeguro(PedidoDecorador):
    def processar_pedido(self) -> str:
        # Adiciona seguro ao pedido
        return self.pedido.processar_pedido() + " + com seguro"

# Proxy - Controla o acesso ao pedido
class ProxyDePedido(Pedido):
    def __init__(self, pedido_real: Pedido):
        self.pedido_real = pedido_real

    def processar_pedido(self) -> str:
        # Aqui você pode verificar permissões ou fazer outras verificações
        print("Verificando se pode processar o pedido...")
        return self.pedido_real.processar_pedido()

# Factory para criar pedidos
class FabricaDePedidos:
    def criar_pedido(self, tipo: str) -> Pedido:
        if tipo == "normal":
            return PedidoNormal(1, "Pedido normal")
        elif tipo == "embrulho":
            return PedidoComEmbrulho(PedidoNormal(2, "Pedido com presente"))
        elif tipo == "seguro":
            return PedidoComSeguro(PedidoNormal(3, "Pedido com seguro"))
        else:
            raise ValueError("Tipo de pedido desconhecido")

# Exemplo de como usar o código
if __name__ == "__main__":
    fabrica = FabricaDePedidos()

    # Criando pedidos usando a fábrica
    pedido_normal = fabrica.criar_pedido("normal")
    pedido_com_embrulho = fabrica.criar_pedido("embrulho")
    pedido_com_seguro = fabrica.criar_pedido("seguro")

    # Usando o Proxy para controlar o acesso ao pedido normal
    proxy_pedido = ProxyDePedido(pedido_normal)

    # Processando os pedidos
    print(proxy_pedido.processar_pedido())  # Exemplo de uso do Proxy
    print(pedido_com_embrulho.processar_pedido())  # Pedido com embrulho
    print(pedido_com_seguro.processar_pedido())  # Pedido com seguro
