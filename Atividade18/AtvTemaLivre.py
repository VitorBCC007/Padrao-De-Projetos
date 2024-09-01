from abc import ABC, abstractmethod

class Pedido(ABC):
    @abstractmethod
    def processar_pedido(self) -> str:
        pass

class PedidoNormal(Pedido):
    def __init__(self, id: int, detalhes: str):
        self.id = id
        self.detalhes = detalhes

    def processar_pedido(self) -> str:
        return f"Pedido {self.id} com detalhes: {self.detalhes} foi processado."

#DECORATOR
class PedidoDecorador(Pedido):
    def __init__(self, pedido: Pedido):
        self.pedido = pedido

    @abstractmethod
    def processar_pedido(self) -> str:
        pass

#DECORATOR
class PedidoComEmbrulho(PedidoDecorador):
    def processar_pedido(self) -> str:
        return self.pedido.processar_pedido() + " + Pedido com embrulho para presente."

#DECORATOR
class PedidoComSeguro(PedidoDecorador):
    def processar_pedido(self) -> str:
        return self.pedido.processar_pedido() + " + Pedido com seguro."

#DECORATOR
class PedidoComFreteExpresso(PedidoDecorador):
    def processar_pedido(self) -> str:
        return self.pedido.processar_pedido() + " + Pedido com frete expresso."

#PROXY
class ProxyDePedido(Pedido):
    def __init__(self, pedido_real: Pedido, usuario: str):
        self.pedido_real = pedido_real
        self.usuario = usuario

    def verificar_permissao(self) -> bool:
        usuarios_autorizados = ["admin", "gerente"]
        return self.usuario in usuarios_autorizados

    def processar_pedido(self) -> str:
        if self.verificar_permissao():
            print("Usuário autorizado. Processando o pedido...")
            return self.pedido_real.processar_pedido()
        else:
            return "Usuário não autorizado a processar o pedido."

# FACTORY
class FabricaDePedidos(ABC):
    @abstractmethod
    def criar_pedido(self, tipo: str) -> Pedido:
        pass

#FACTORY
class FabricaDePedidosConcreta(FabricaDePedidos):
    def criar_pedido(self, tipo: str) -> Pedido:
        if tipo == "normal":
            return PedidoNormal(1, "Pedido normal sem extras")
        elif tipo == "embrulho":
            return PedidoComEmbrulho(PedidoNormal(2, "Pedido com presente"))
        elif tipo == "seguro":
            return PedidoComSeguro(PedidoNormal(3, "Pedido com seguro"))
        elif tipo == "frete":
            return PedidoComFreteExpresso(PedidoNormal(4, "Pedido com frete expresso"))
        elif tipo == "completo":
            pedido = PedidoNormal(5, "Pedido completo")
            pedido = PedidoComEmbrulho(pedido)
            pedido = PedidoComSeguro(pedido)
            pedido = PedidoComFreteExpresso(pedido)
            return pedido
        else:
            raise ValueError("Tipo de pedido desconhecido")

if __name__ == "__main__":
    fabrica = FabricaDePedidosConcreta()

    pedido_normal = fabrica.criar_pedido("normal")
    pedido_com_embrulho = fabrica.criar_pedido("embrulho")
    pedido_com_seguro = fabrica.criar_pedido("seguro")
    pedido_com_frete = fabrica.criar_pedido("frete")
    pedido_completo = fabrica.criar_pedido("completo")

    print(pedido_normal.processar_pedido())  
    print(pedido_com_embrulho.processar_pedido())  
    print(pedido_com_seguro.processar_pedido())  
    print(pedido_com_frete.processar_pedido())  
    print(pedido_completo.processar_pedido())  

    print('----------------------------------------------------------------------------------')

    # PROXY PARA CONTROLAR ACESSO
    proxy_pedido = ProxyDePedido(pedido_normal, "admin")  # AUTORIZADO
    print(proxy_pedido.processar_pedido())
    
    print('----------------------------------------------------------------------------------')

    proxy_pedido_nao_autorizado = ProxyDePedido(pedido_completo, "cliente")  # NAO
    print(proxy_pedido_nao_autorizado.processar_pedido())
