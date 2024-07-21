import re

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, login, senha):
        if self.successor:
            return self.successor.handle(login, senha)
        return True

class LoginCadastradoHandler(Handler):
    def __init__(self, logins_cadastrados, successor=None):
        super().__init__(successor)
        self.logins_cadastrados = logins_cadastrados

    def handle(self, login, senha):
        if login not in self.logins_cadastrados:
            print("Login não cadastrado.")
            return False
        return super().handle(login, senha)

class MaiusculaHandler(Handler):
    def handle(self, login, senha):
        if not any(c.isupper() for c in senha):
            print("A senha deve conter pelo menos uma letra maiuscula")
            return False
        return super().handle(login, senha)

class MinusculaHandler(Handler):
    def handle(self, login, senha):
        if not any(c.islower() for c in senha):
            print("A senha deve conter pelo menos uma letra minúscula.")
            return False
        return super().handle(login, senha)

class CaractereEspecialHandler(Handler):
    def handle(self, login, senha):
        if not any(c in '@#$%&*' for c in senha):
            print("A senha deve conter pelo menos um caractere especial (@, #, $, %, &, *).")
            return False
        return super().handle(login, senha)

class NumeroHandler(Handler):
    def handle(self, login, senha):
        if not any(c.isdigit() for c in senha):
            print("A senha deve conter pelo menos um número.")
            return False
        return super().handle(login, senha)

class NumerosConsecutivosHandler(Handler):
    def handle(self, login, senha):
        if re.search(r'\d{3}', senha):
            print("A senha não pode conter 3 números consecutivos.")
            return False
        return super().handle(login, senha)

class TamanhoMinimoHandler(Handler):
    def handle(self, login, senha):
        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            return False
        return super().handle(login, senha)

class TamanhoMaximoHandler(Handler):
    def handle(self, login, senha):
        if len(senha) > 16:
            print("A senha não pode ter mais de 16 caracteres.")
            return False
        return super().handle(login, senha)

logins_cadastrados = ["usuario1", "usuario2", "usuario3"]

handler = LoginCadastradoHandler(logins_cadastrados)
handler = MaiusculaHandler(handler)
handler = MinusculaHandler(handler)
handler = CaractereEspecialHandler(handler)
handler = NumeroHandler(handler)
handler = NumerosConsecutivosHandler(handler)
handler = TamanhoMinimoHandler(handler)
handler = TamanhoMaximoHandler(handler)

login = "usuario1"
senha = "abc123"

# login = "usuario1"
# senha = "Morango52@"

if handler.handle(login, senha):
    print("Login e senha validos")
else:
    print("Login e/ou senha invalidos")

#PARA VALIDAR UM LOGIN E SENHA SIGA TODAS AS REQUISICOES ABAIXO:
#sem uma letra maiuscula  ==  invalido
#numeros seguidos (sequencia)  ==   invalido 
#senha sem 8 caracteres == invalido
#senha sem 1 numero == invalido
#senha sem letra minuscula == invalido
#senha sem 1 caracter especial == invalido

#login fora dos cadastros == logins_cadastrados = ["usuario1", "usuario2", "usuario3"]
# if login not in self.logins_cadastrados:
            #print("Login não cadastrado.")
