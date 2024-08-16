import csv

produtos = {}

# Bloco para criar/manipular o arquivo csv 

def criar_arquivo_csv(nome_arquivo='relatorio_estoque.csv'):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerow(['ID', 'Nome', 'Categoria', 'Preço', 'Quantidade', 'Descrição'])
    return {}

def carregar_produtos(nome_arquivo='relatorio_estoque.csv'):
    produtos = {}
    with open(nome_arquivo, mode='r', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=';')
            for linha in leitor_csv:
                if linha:
                    id_produto, nome, categoria, preco, quantidade_estoque, descricao = linha
                    produtos[id_produto] = {
                        'nome': nome,
                        'categorias': categoria,
                        'preco': float(preco),
                        'quantidade_estoque': int(quantidade_estoque),
                        'descricao': descricao    
                    }
    return produtos

def salvar_produtos(produtos, nome_arquivo='relatorio_estoque.csv'):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerow(['ID', 'Nome', 'Categoria', 'Preço', 'Quantidade', 'Descrição'])
        for id_produto, dados in produtos.items():
            escritor_csv.writerow([
                id_produto,
                dados['nome'],
                dados['categorias'],
                dados['preco'],
                dados['quantidade_estoque'],
                dados['descricao']
            ])

# Bloco para criar e manipular o estoque
def menu():
    menu = '''
    ---------------------------
            New System
    ---------------------------
    1 - Cadastrar Novo Produto
    2 - Listar Produtos Cadastrados
    3 - Atualizar Cadastro de Produtos
    4 - Remover Cadastro de Produto
    5 - Adicionar Carrinho de compras
    6 - Imprimir Relatórios
    7 - Sair
    '''

    while True:
        opcao = input(f'{menu}\nEscolha uma opção acima: ')

        if opcao == '1':
            cadastrar_produto(produtos)
            salvar_produtos(produtos)

        elif opcao == '2':
            imprimir_produtos(produtos)

        elif opcao == '3':
            alterar_produto(produtos)
            salvar_produtos(produtos)

        elif opcao == '4':
            remover_produto(produtos)
            salvar_produtos(produtos)

        elif opcao == '5':
            print(produtos)#fazer a função vendas

        elif opcao == '6':
            gerar_relatorio_csv(produtos)

        elif opcao == '7':
            break

        else:
            print("Opção inválida. Tente novamente.")

def gerar_id(produtos):
    ultimo_id = len(produtos)
    novo_id = ultimo_id + 1
    return f'{novo_id:04d}'

def selecionar_categoria(categorias):
    print("Selecione uma categoria de produto:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    escolha = int(input("Digite o número da categoria desejada: "))
    return categorias[escolha - 1]

def cadastrar_produto(produtos):
    while True:
        id_produto = gerar_id(produtos)
        produtos[id_produto] = {
            'nome': input('Digite o nome do produto: '),
            'categorias': selecionar_categoria(['Informática', 'Roupas', 'Papelaria', 'Livros', 'Brinquedos']),
            'preco': float(input('Digite o preço do produto: ')),
            'quantidade_estoque': int(input('Digite a quantidade do produto: ')),
            'descricao': input('Digite uma breve descrição do produto: ')
        }
        continuar = input("Deseja adicionar outro produto? (s/n): ").strip().lower()
        if continuar != 's':
            break

def alterar_produto(produtos):
    imprimir_produtos(produtos)
    
    id_produto = input('Digite o ID do produto que deseja alterar: ')
    
    if id_produto in produtos:
        print(f'Produto escolhido: {produtos[id_produto]}')
        print('''
        O que deseja atualizar?
        1 - Nome
        2 - Categoria
        3 - Preço
        4 - Quantidade
        5 - Descrição
        6 - Todas as informações
        ''')
        sub_opcao = input('Escolha uma opção acima: ')

        if sub_opcao == '1':
            nome = input('Digite o novo nome: ')
            produtos[id_produto]['nome'] = nome
        elif sub_opcao == '2':
            categoria = selecionar_categoria(['Informática', 'Roupas', 'Papelaria', 'Livros'])
            produtos[id_produto]['categorias'] = categoria
        elif sub_opcao == '3':
            preco = float(input('Digite o novo preço: '))
            produtos[id_produto]['preco'] = preco
        elif sub_opcao == '4':
            quantidade_estoque = int(input('Digite a nova quantidade: '))
            produtos[id_produto]['quantidade_estoque'] = quantidade_estoque
        elif sub_opcao == '5':
            descricao = input('Digite a nova descrição: ')
            produtos[id_produto]['descricao'] = descricao
        elif sub_opcao == '6':
            nome = input('Digite o novo nome: ')
            categoria = selecionar_categoria(['Informática', 'Roupas', 'Papelaria', 'Livros'])
            preco = float(input('Digite o novo preço: '))
            quantidade_estoque = int(input('Digite a nova quantidade: '))
            descricao = input('Digite a nova descrição: ')
            
            produtos[id_produto]['nome'] = nome
            produtos[id_produto]['categorias'] = categoria
            produtos[id_produto]['preco'] = preco
            produtos[id_produto]['quantidade_estoque'] = quantidade_estoque
            produtos[id_produto]['descricao'] = descricao
        else:
            print('Opção inválida.')
            return

        print('Produto atualizado com sucesso.')
    else:
        print('Produto não encontrado.')

def imprimir_produtos(produtos):
    for chave, dados_produto in produtos.items():
        print(f'ID: {chave}')
        for campo, valor in dados_produto.items():
            print(f'  {campo.capitalize()}: {valor}')
        print('-' * 30)

def gerar_relatorio_csv(produtos, nome_arquivo='relatorio_estoque.csv'):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerow(['ID', 'Nome', 'Categoria', 'Preço', 'Quantidade', 'Descrição'])
        for id_produto, dados in produtos.items():
            escritor_csv.writerow([
                id_produto,
                dados['nome'],
                dados['categorias'],
                dados['preco'],
                dados['quantidade_estoque'],
                dados['descricao']
            ])
    print(f'Relatório gerado e salvo como {nome_arquivo}')

def remover_produto(produtos):
    id_produto = input('Digite o ID do produto que deseja remover: ')
    if id_produto in produtos:
        produtos.pop(id_produto)
        print('Produto removido com sucesso.')
    else:
        print('Produto não encontrado.')

produtos = criar_arquivo_csv()

menu()