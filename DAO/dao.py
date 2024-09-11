from models import Produto

class ProdutoDAO:
    def __init__(self):
        self.produtos = []

    def criar_produto(self, produto):
        """Adiciona um novo produto à lista."""
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado com sucesso.")

    def obter_todos_produtos(self):
        """Retorna todos os produtos."""
        return self.produtos

    def buscar_produto_por_id(self, id_produto):
        """Busca um produto pelo ID."""
        return next((produto for produto in self.produtos if produto.id_produto == id_produto), None)

    def atualizar_produto(self, id_produto, nome, preco):
        """Atualiza as informações de um produto."""
        produto = self.buscar_produto_por_id(id_produto)
        if produto:
            produto.nome = nome
            produto.preco = preco
            print(f"Produto ID '{id_produto}' atualizado com sucesso.")
        else:
            print(f"Produto ID '{id_produto}' não encontrado.")

    def deletar_produto(self, id_produto):
        """Remove um produto pelo ID."""
        produto = self.buscar_produto_por_id(id_produto)
        if produto:
            self.produtos.remove(produto)
            print(f"Produto ID '{id_produto}' removido com sucesso.")
        else:
            print(f"Produto ID '{id_produto}' não encontrado.")
