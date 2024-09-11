from dao import ProdutoDAO
from models import Produto

class ControladorProduto:
    def __init__(self):
        self.dao = ProdutoDAO()

    def adicionar_produto(self, id_produto, nome, preco):
        """Adiciona um novo produto usando o DAO."""
        produto = Produto(id_produto, nome, preco)
        self.dao.criar_produto(produto)

    def listar_produtos(self):
        """Lista todos os produtos."""
        produtos = self.dao.obter_todos_produtos()
        if produtos:
            print("\nLista de Produtos:")
            for produto in produtos:
                print(f"ID: {produto.id_produto}, Nome: {produto.nome}, Preço: {produto.preco}")
        else:
            print("Nenhum produto encontrado.")

    def atualizar_produto(self, id_produto, nome, preco):
        """Atualiza um produto existente."""
        self.dao.atualizar_produto(id_produto, nome, preco)

    def remover_produto(self, id_produto):
        """Remove um produto existentee"""
        self.dao.deletar_produto(id_produto)
