# app.py

from controller import ProductController

def main():
    controller = ProductController()

    while True:
        print('----------------------------')
        print("      Menu de Opções:")
        print('----------------------------')
        print("\n")

        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            product_id = int(input("Digite o ID do produto: "))
            name = input("Digite o nome do produto: ")
            price = float(input("Digite o preço do produto: "))
            controller.add_product(product_id, name, price)
        
        elif choice == '2':
            controller.list_products()
        
        elif choice == '3':
            product_id = int(input("Digite o ID do produto a ser atualizado: "))
            name = input("Digite o novo nome do produto: ")
            price = float(input("Digite o novo preço do produto: "))
            controller.update_product(product_id, name, price)
        
        elif choice == '4':
            product_id = int(input("Digite o ID do produto a ser removido: "))
            controller.delete_product(product_id)
        
        elif choice == '5':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    main()
