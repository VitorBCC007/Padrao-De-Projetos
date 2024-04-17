import random
import string

class GerenciadorLogin:
    _instancia = None

    def __new__(cls):  #GARANTE CRIAÇÃO E RETORNO 
        if cls._instancia is None: #_INSTANCIA CRIADA?
            cls._instancia = super().__new__(cls) #PAI (((SUPER))) CRIA NOVA INSTANCIA 
            cls._instancia.logado = False 
        return cls._instancia

    def login(self):
        if not self.logado:
            nome_usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")

            codigo_bot = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=6))
            print("Para evitar bots, digite o seguinte código: ")
            print(codigo_bot)

            entrada_usuario = input("Digite o código de verificação: ")

            if entrada_usuario == codigo_bot:
                print("\nLogin bem-sucedido!")
                self.logado = True
            else:
                print("\nTe peguei BOT!")
        else:
            print("\n[[Você já está logado]]")

    def logout(self):
        if self.logado:
            print("\nLogout realizado, entre com [1] para trocar de conta")
            self.logado = False
        else: 
            print("\n[[Você já está deslogado]]")

if __name__ == "__main__":
    gerenciador_login = GerenciadorLogin()

    while True:
        print("\nEscolha uma opção:\n")
        print("[1] - Login")
        print("[2] - Logout")
        print("[3] - Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            gerenciador_login.login()
        elif escolha == "2":
            gerenciador_login.logout()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("1 2 ou 3")
