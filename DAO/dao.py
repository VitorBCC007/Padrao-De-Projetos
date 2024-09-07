# dao.py

from models import Product

class ProductDAO:
    def __init__(self):
        # Simulando um banco de dados com uma lista
        self.products = []

    def create_product(self, product):
        """Adiciona um novo produto à lista."""
        self.products.append(product)
        print(f"Produto '{product.name}' adicionado com sucesso.")

    def get_all_products(self):
        """Retorna todos os produtos."""
        return self.products

    def find_product_by_id(self, product_id):
        """Busca um produto pelo ID."""
        return next((product for product in self.products if product.product_id == product_id), None)

    def update_product(self, product_id, name, price):
        """Atualiza as informações de um produto."""
        product = self.find_product_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            print(f"Produto ID '{product_id}' atualizado com sucesso.")
        else:
            print(f"Produto ID '{product_id}' não encontrado.")

    def delete_product(self, product_id):
        """Remove um produto pelo ID."""
        product = self.find_product_by_id(product_id)
        if product:
            self.products.remove(product)
            print(f"Produto ID '{product_id}' removido com sucesso.")
        else:
            print(f"Produto ID '{product_id}' não encontrado.")
