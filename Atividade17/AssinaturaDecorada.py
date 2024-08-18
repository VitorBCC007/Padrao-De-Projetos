from abc import ABC, abstractmethod

class Assinatura(ABC):
    @abstractmethod
    def descricao(self):
        pass
    
    @abstractmethod
    def preco(self):
        pass

class AssinaturaBase(Assinatura):
    def descricao(self):
        return "Assinatura Base: Assistir vídeos em um único dispositivo"
    
    def preco(self):
        return 9.99

class PacoteDecorator(Assinatura):
    def __init__(self, assinatura):
        self._assinatura = assinatura
    
    @abstractmethod
    def descricao(self):
        pass
    
    @abstractmethod
    def preco(self):
        pass

class PacoteMultiplosDispositivos(PacoteDecorator):
    def descricao(self):
        return self._assinatura.descricao() + " + Pacote: Assistir vídeos em vários dispositivos"
    
    def preco(self):
        return self._assinatura.preco() + 19.99

class PacoteFreteGratis(PacoteDecorator):
    def descricao(self):
        return self._assinatura.descricao() + " + Pacote: Frete grátis em produtos"
    
    def preco(self):
        return self._assinatura.preco() + 9.99  

class PacoteCaixaSurpresa(PacoteDecorator):
    def descricao(self):
        return self._assinatura.descricao() + " + Pacote: Caixa surpresa com produtos relacionados a filmes e séries"
    
    def preco(self):
        return self._assinatura.preco() + 29.99

class PacoteCartaoPlatinum(PacoteDecorator):
    def descricao(self):
        return self._assinatura.descricao() + " + Pacote: Cartão de crédito Platinum"
    
    def preco(self):
        return self._assinatura.preco() + 49.99

class PacoteCashBack(PacoteDecorator):
    def descricao(self):
        return self._assinatura.descricao() + " + Pacote: Compra com Cash Back"
    
    def preco(self):
        return self._assinatura.preco() + 19.99

def exibir_assinatura(assinatura):
    print(f"Descrição: {assinatura.descricao()}")
    print(f"Preço Total: R${assinatura.preco():.2f}")

#MENU
def menu():
    print("Escolha a assinatura:")
    print("1. Assinatura Base - R$9,99") #OBRIGATORIO

    
    pacotes = {
        2: PacoteMultiplosDispositivos,
        3: PacoteFreteGratis,
        4: PacoteCaixaSurpresa,
        5: PacoteCartaoPlatinum,
        6: PacoteCashBack
    }
    #MENU
    print("\nEscolha os pacotes adicionais (digite 0 para finalizar a compra):")
    print("2. Pacote: Assistir vídeos em vários dispositivos - R$19,99")
    print("3. Pacote: Frete grátis em produtos - R$9,99")
    print("4. Pacote: Caixa surpresa com produtos relacionados a filmes e séries - R$29,99")
    print("5. Pacote: Cartão de crédito Platinum - R$49,99")
    print("6. Pacote: Compra com Cash Back - R$19,99")
    print("0. Finalizar compra")
    assinatura = None
    escolha_pacotes = set()
    
#[[[[[[[[[[[[[[[OBSERVACAO]]]]]]]]]]]]]]]
#O Usuário pode escolher só a assinatura do stream ou adicionar quantos pacotes quiser na sua assinatura, desde que não sejam repetidos.
#OBRIGATORIO COMPRAR A ASSINATURA BASE DO STREAM
#APOS ESCOLHER A ASSINATURA BASE ELE PODE ADICIONAR PACOTES A SUA ASSINATURA
#NAO PODENDO REPETIR NENHUM PACOTE 
    
    while True:
        try:
            if assinatura is None:
                escolha = int(input("\nDigite a opção da assinatura base (1) ou 0 para finalizar a compra: "))
                if escolha == 0:
                    print("Compra finalizada sem assinatura.")
                    return
                elif escolha == 1:
                    assinatura = AssinaturaBase()
                    print("\nAssinatura Base selecionada.")
                else:
                    print("Escolha inválida. Tente novamente.")
            else:
                escolha = int(input("\nDigite a opção do pacote adicional ou 0 para finalizar a compra: "))
                if escolha == 0:
                    break
                if escolha in pacotes and escolha not in escolha_pacotes:
                    escolha_pacotes.add(escolha)
                    pacote_selecionado = pacotes[escolha](assinatura)
                    print(f"Pacote '{pacote_selecionado.descricao().split(' + Pacote: ')[-1]}' adicionado.")
                elif escolha in escolha_pacotes:
                    print("Pacote já adicionado. Escolha outro ou finalize.")
                else:
                    print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    for pacote in escolha_pacotes:
        assinatura = pacotes[pacote](assinatura)
    
    exibir_assinatura(assinatura)
menu()

#[[[[[[[[[[[[[[[OBSERVACAO]]]]]]]]]]]]]]]
#O Usuário pode escolher só a assinatura do stream ou adicionar quantos pacotes quiser na sua assinatura, desde que não sejam repetidos.
#OBRIGATORIO COMPRAR A ASSINATURA BASE DO STREAM
#APOS ESCOLHER A ASSINATURA BASE ELE PODE ADICIONAR PACOTES A SUA ASSINATURA
#NAO PODENDO REPETIR NENHUM PACOTE 
