from models import Usuario, BancoDeDadosUsuario
from views import VisaoUsuario

class ControladorUsuario:
    def __init__(self):
        self.banco_dados = BancoDeDadosUsuario()
        self.visao = VisaoUsuario()

    def adicionar_usuario(self):
        nome, email = self.visao.obter_input_usuario()
        usuario_id = len(self.banco_dados.obter_todos_usuarios()) + 1
        usuario = Usuario(usuario_id, nome, email)
        self.banco_dados.adicionar_usuario(usuario)
        print("Usuário adicionado com sucesso! !\n")

    def listar_usuarios(self):
        usuarios = self.banco_dados.obter_todos_usuarios()
        self.visao.exibir_lista_usuarios(usuarios)

    def buscar_usuario(self):
        usuario_id = self.visao.obter_input_id_usuario()
        usuario = self.banco_dados.buscar_usuario(usuario_id)
        self.visao.exibir_usuario(usuario)

#CONTROLE DE FLUXO MODEL E VIEW
    def executar(self):
        while True:
            escolha = self.visao.exibir_menu()
            if escolha == '1':
                self.adicionar_usuario()
            elif escolha == '2':
                self.listar_usuarios()
            elif escolha == '3':
                self.buscar_usuario()
            elif escolha == '4':
                print("Saindo do sistema. . .")
                break
            else:
                print("Opção inválida! Tente novamente")

if __name__ == '__main__':
    controlador = ControladorUsuario()
    controlador.executar()
