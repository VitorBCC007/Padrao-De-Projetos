from controller import ControladorProduto

def main():
    controlador = ControladorProduto()

    while True:
        print('----------------------------')
        print("      Menu de Opções:")
        print('----------------------------\n')

        print("[1] - Adicionar Produto")
        print("[2] - Listar Produtos")
        print("[3] - Atualizar Produto")
        print("[4] - Remover Produto")
        print("[5] - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try:
                id_produto = int(input("Digite o ID do produto: "))
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                controlador.adicionar_produto(id_produto, nome, preco)
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar números para o ID e o preço.")
        
        elif opcao == '2':
            controlador.listar_produtos()
        
        elif opcao == '3':
            try:
                id_produto = int(input("Digite o ID do produto a ser atualizado: "))
                nome = input("Digite o novo nome do produto: ")
                preco = float(input("Digite o novo preço do produto: "))
                controlador.atualizar_produto(id_produto, nome, preco)
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar números para o ID e o preço.")
        
        elif opcao == '4':
            try:
                id_produto = int(input("Digite o ID do produto a ser removido: "))
                controlador.remover_produto(id_produto)
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar um número para o ID.")
        
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    main()
