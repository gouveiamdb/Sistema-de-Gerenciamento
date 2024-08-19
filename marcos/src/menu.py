#funcao do menu principal
from src.compra import adicionar_ao_carrinho, finalizar_compra, gerar_relatorio_vendas, visualizar_carrinho
from src.produto import cadastrar_produto, alterar_produto, imprimir_produtos, remover_produto
from src.arquivo_csv import carregar_produtos, salvar_produtos, gerar_relatorio_csv

def menu():
    produtos = carregar_produtos()
    
    menu = '''
    ---------------------------
            New System
    ---------------------------
    1 - Cadastrar Novo Produto
    2 - Listar Produtos Cadastrados
    3 - Atualizar Cadastro de Produtos
    4 - Remover Cadastro de Produto
    5 - Adicionar ao Carrinho de Compras
    6 - Visualizar Carrinho
    7 - Finalizar Compra
    8 - Gerar Relatório de Estoque
    9 - Gerar Relatório de Vendas
    10 - Sair
    '''

    while True:
        opcao = input(f'{menu}\nEscolha uma opção acima: ')

        if opcao == '1':
            cadastrar_produto(produtos)

        elif opcao == '2':
            imprimir_produtos(produtos)

        elif opcao == '3':
            alterar_produto(produtos)

        elif opcao == '4':
            remover_produto(produtos)

        elif opcao == '5':
            carrinho = adicionar_ao_carrinho(produtos, carrinho)

        elif opcao == '6':
            carrinho = visualizar_carrinho(carrinho, produtos)

        elif opcao == '7':
            carrinho = finalizar_compra(produtos, carrinho)

        elif opcao == '8':
            gerar_relatorio_csv(produtos)

        elif opcao == '9':
            gerar_relatorio_vendas(carrinho)

        elif opcao == '10':
            salvar_produtos(produtos)
            break

        else:
            print("Opção inválida. Tente novamente.")
