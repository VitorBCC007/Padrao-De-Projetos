# controller.py

from dao import ProductDAO
from models import Product

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def add_product(self, product_id, name, price):
        """Adiciona um novo produto usando o DAO."""
        product = Product(product_id, name, price)
        self.dao.create_product(product)

    def list_products(self):
        """Lista todos os produtos."""
        products = self.dao.get_all_products()
        if products:
            print("\nLista de Produtos:")
            for product in products:
                print(f"ID: {product.product_id}, Nome: {product.name}, Preço: {product.price}")
        else:
            print("Nenhum produto encontrado.")

    def update_product(self, product_id, name, price):
        """Atualiza um produto existente."""
        self.dao.update_product(product_id, name, price)

    def delete_product(self, product_id):
        """Remove um produto existente."""
        self.dao.delete_product(product_id)
