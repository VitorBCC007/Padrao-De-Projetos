class VisaoUsuario:
    @staticmethod
    def exibir_lista_usuarios(usuarios):
        print("\nLista de Usuários:")
        for usuario in usuarios:
            print(f"ID: {usuario.usuario_id}, Nome: {usuario.nome}, Email: {usuario.email}")
        print("\n")

    @staticmethod
    def exibir_usuario(usuario):
        if usuario:
            print(f"Usuário encontrado: ID: {usuario.usuario_id}, Nome: {usuario.nome}, Email: {usuario.email}")
        else:
            print("Usuário não encontrado")

    @staticmethod
    def obter_input_usuario():
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        return nome, email

    @staticmethod
    def obter_input_id_usuario():
        return int(input("Digite o ID do usuário que deseja buscar: "))

    @staticmethod
    def exibir_menu():
        print('----------------------------------------------')
        print("\n[1] - Adicionar Usuário")
        print("[2] - Listar Usuários")
        print("[3] - Buscar Usuário por ID")
        print("[4] - Sair")
        return input("Escolha uma opção: ")
        print('----------------------------------------------')

