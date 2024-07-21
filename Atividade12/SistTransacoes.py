from abc import ABC, abstractmethod

class ManipuladorDeTransacao(ABC):
    @abstractmethod
    def definir_proximo(self, handler):
        pass
    
    @abstractmethod
    def manipular(self, request):
        pass

class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

class ManipuladorDeposito(ManipuladorDeTransacao):
    def __init__(self):
        self._proximo_manipulador = None
        self.limite_maximo_deposito = 10000  
    
    def definir_proximo(self, handler):
        self._proximo_manipulador = handler
        return handler
    
    def manipular(self, request):
        if request['tipo'] == 'deposito':
            if request['quantia'] > 0:
                if request['quantia'] <= self.limite_maximo_deposito:
                    request['conta'].saldo += request['quantia']
                    print(f"Deposito de {request['quantia']} processado. Novo saldo: {request['conta'].saldo}")
                else:
                    print(f"Quantia de deposito excede o limite maximo de {self.limite_maximo_deposito}.")
            else:
                print("Quantia de deposito invalida.")
        elif self._proximo_manipulador:
            self._proximo_manipulador.manipular(request)

class ManipuladorSaque(ManipuladorDeTransacao):
    def __init__(self):
        self._proximo_manipulador = None
        self.limite_maximo_saque = 500  
    
    def definir_proximo(self, handler):
        self._proximo_manipulador = handler
        return handler
    
    def manipular(self, request):
        if request['tipo'] == 'saque':
            if request['quantia'] > 0 and request['conta'].saldo >= request['quantia']:
                if request['quantia'] <= self.limite_maximo_saque:
                    request['conta'].saldo -= request['quantia']
                    print(f"Saque de {request['quantia']} processado. Novo saldo: {request['conta'].saldo}")
                else:
                    print(f"Quantia de saque excede o limite máximo de {self.limite_maximo_saque}.")
            else:
                print("Quantia de saque invalida ou fundos insuficientes.")
        elif self._proximo_manipulador:
            self._proximo_manipulador.manipular(request)

class ManipuladorTransferencia(ManipuladorDeTransacao):
    def __init__(self):
        self._proximo_manipulador = None
    
    def definir_proximo(self, handler):
        self._proximo_manipulador = handler
        return handler
    
    def manipular(self, request):
        if request['tipo'] == 'transferencia':
            if request['quantia'] > 0 and request['conta_origem'].saldo >= request['quantia']:
                request['conta_origem'].saldo -= request['quantia']
                request['conta_destino'].saldo += request['quantia']
                print(f"Transferencia de {request['quantia']} processada. Novo saldo da conta origem: {request['conta_origem'].saldo}, Novo saldo da conta destino: {request['conta_destino'].saldo}")
            else:
                print("Quantia de transferencia inválida ou fundos insuficientes.")
        elif self._proximo_manipulador:
            self._proximo_manipulador.manipular(request)

class Cliente:
    def __init__(self):
        self.cadeia = ManipuladorDeposito()
        self.cadeia.definir_proximo(ManipuladorSaque()).definir_proximo(ManipuladorTransferencia())
    
    def processar_transacao(self, request):
        self.cadeia.manipular(request)

if __name__ == "__main__":
    conta1 = Conta(saldo=1000)
    conta2 = Conta(saldo=500)
    cliente = Cliente()
    
    # Depósito
    cliente.processar_transacao({'tipo': 'deposito', 'quantia': 200, 'conta': conta1})
    
    # Saque
    cliente.processar_transacao({'tipo': 'saque', 'quantia': 150, 'conta': conta1})
    
    # Transferencia c1 p c2
    cliente.processar_transacao({'tipo': 'transferencia', 'quantia': 300, 'conta_origem': conta1, 'conta_destino': conta2})
    
    # Transação invalida
    cliente.processar_transacao({'tipo': 'invalido', 'quantia': 100, 'conta': conta1})
    
    # Transferência c2 p c1
    cliente.processar_transacao({'tipo': 'transferencia', 'quantia': 10, 'conta_origem': conta2, 'conta_destino': conta1})
    
    # Deposito acima do limite  ((( self.limite_maximo_deposito = 10000 )))
    cliente.processar_transacao({'tipo': 'deposito', 'quantia': 15000, 'conta': conta1})
    
    #OBS: sacando + que o limite ((( self.limite_maximo_saque = 500 ))) 
    cliente.processar_transacao({'tipo': 'saque', 'quantia': 600, 'conta': conta1})
#ALTERAR VALOR DOLIMITE PARA PODER REALIZAR +QUANTIA (deposito e saque)
