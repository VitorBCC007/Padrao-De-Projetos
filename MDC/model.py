class Usuario:
    def __init__(self, usuario_id, nome, email):
        self.usuario_id = usuario_id
        self.nome = nome
        self.email = email

class BancoDeDadosUsuario:   #< < < lógica de negocios
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def obter_todos_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, usuario_id):
        return next((usuario for usuario in self.usuarios if usuario.usuario_id == usuario_id), None)
