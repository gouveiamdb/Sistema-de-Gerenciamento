from src.arquivo_csv import salvar_produtos, gerar_relatorio_estoque, gerar_relatorio_vendas #gerar_relatorio_csv
from src.produto import imprimir_produtos


def adicionar_ao_carrinho(produtos, carrinho):
    while True:
        imprimir_produtos(produtos)
        id_produto = input('Digite o ID do produto que deseja adicionar ao carrinho: ')
        if id_produto in produtos:
            try:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= produtos[id_produto]['quantidade_estoque']:
                    carrinho.append({
                        'id': id_produto,
                        'nome': produtos[id_produto]['nome'],
                        'quantidade': quantidade,
                        'preco_unitario': produtos[id_produto]['preco']
                    })
                    print('Produto adicionado ao carrinho.')
                else:
                    print('Quantidade desejada excede o estoque disponível.')
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")
        else:
            print('Produto não encontrado.')

        confirmar = input("Confirma essa operação? (s/n): ").strip().lower()
        if confirmar != 's':
            break
    return carrinho
 

def excluir_do_carrinho(carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
        return carrinho
    id_produto = input('Digite o ID do produto que deseja remover do carrinho: ')
    carrinho = [item for item in carrinho if item['id'] != id_produto]
    print('Produto removido do carrinho.')
    return carrinho


def alterar_quantidade_carrinho(carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
        return carrinho
    id_produto = input('Digite o ID do produto cuja quantidade deseja alterar: ')
    for item in carrinho:
        if item['id'] == id_produto:
            try:
                nova_quantidade = int(input('Digite a nova quantidade: '))
                if nova_quantidade <= 0:
                    print("Quantidade inválida.")
                else:
                    item['quantidade'] = nova_quantidade
                    print('Quantidade atualizada.')
                return carrinho
            except ValueError:
                print("Por favor, insira um número válido para a nova quantidade.")
    print('Produto não encontrado no carrinho.')
    return carrinho


def visualizar_carrinho(carrinho, produtos):
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        while True:
            print("Carrinho de Compras:")
            total = 0
            for item in carrinho:
                valor_total = item['quantidade'] * item['preco_unitario']
                total += valor_total
                print(f"{item['nome']} - Quantidade: {item['quantidade']}, Preço Unitário: {item['preco_unitario']:.2f}, Valor Total: {valor_total:.2f}")
            print(f"Total da compra: {total:.2f}")
            print("1 - Excluir produto do carrinho")
            print("2 - Alterar quantidade de produto no carrinho")
            print("3 - Sair")
            
            sub_opcao = input("Escolha uma opção: ")
            
            if sub_opcao == '1':
                carrinho = excluir_do_carrinho(carrinho)
            elif sub_opcao == '2':
                carrinho = alterar_quantidade_carrinho(carrinho)
            elif sub_opcao == '3':
                print("Saindo do carrinho...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    
    return carrinho


def finalizar_compra(produtos, carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
        return carrinho
    
    confirmar = input("Deseja concretizar a compra? (s/n): ").strip().lower()
    if confirmar == 's':
        detalhes_venda = []
        for item in carrinho:
            id_produto = item['id']
            if produtos[id_produto]['quantidade_estoque'] >= item['quantidade']:
                produtos[id_produto]['quantidade_estoque'] -= item['quantidade']
                detalhes_venda.append({
                    'nome': item['nome'],
                    'quantidade_vendida': item['quantidade'],
                    'preco_unitario': item['preco_unitario'],
                    'valor_total': item['quantidade'] * item['preco_unitario']
                })
            else:
                print(f"Quantidade do produto {item['nome']} não disponível no estoque.")
        gerar_relatorio_vendas(detalhes_venda)
        gerar_relatorio_estoque(produtos)
        salvar_produtos(produtos)
        print("Compra finalizada com sucesso.")
        carrinho.clear()
    else:
        print("Compra cancelada.")
    return carrinho
