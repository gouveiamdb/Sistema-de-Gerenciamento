produtos = {}
menu()

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
            produto = cadastrar_produto(produtos)

        elif opcao == '2':
            imprimir_produtos(produtos)

        elif opcao == '3':
            produtos['id_produto'] = input('Digite o código do produto: ')
            if produtos in id_produto.keys():
                print(f'Produto escolhido: {produtos[id_produto]}')
                print('''
          O que deseja atualizar?
            1 - Nome
            2 - Preço
            3 - Quantidade
            4 - Descrição
            5 - Todas as informações
          ''')
                sub_opcao = input('Escolha uma opção acima: ')

                if sub_opcao == '1':
                    nome = input('Digite o novo nome: ')
                    produtos[id_produto]['nome'] = nome
                elif sub_opcao == '2':
                    preco = float(input('Digite o novo preço: '))
                    produtos[id_produto]['preco'] = preco
                elif sub_opcao == '3':
                    quantidade_estoque = int(input('Digite a quantidade: '))
                    produtos[id_produto]['quantidade_estoque'] = quantidade_estoque
                elif sub_opcao == '4':
                    descricao = input('Digite a nova descrição: ')
                    produtos[id_produto]['descricao'] = descricao
                elif sub_opcao == '5':
                    nome = input('Digite o novo nome: ')
                    preco = float(input('Digite o novo preço: '))
                    quantidade = int(input('Digite a quantidade: '))
                    descricao = input('Digite a nova descrição: ')
                    produtos[id_produto]['nome'] = nome
                    produtos[id_produto]['preco'] = preco
                    produtos[id_produto]['quantidade_estoque'] = quantidade_estoque
                    produtos[id_produto]['descricao'] = descricao
                else:
                    print('Nenhuma opção escolhida.')
                    continue

                print('Cadastro do aluno atualizado com sucesso.')
            else:
                print('O aluno não foi encontrado.')
                continue

        elif opcao == '4':
            alunos.pop(input('Digite a matrícula do aluno: '), 'O aluno não foi encontrado.')

        elif opcao == '5':
            print(alunos)

        else:
            break

def gerar_id(ultimo_id):
    if ultimo_id:
        ultimo_id += 1
    else:
        ultimo_id = 1
    return f'{ultimo_id:04d}'

def selecionar_categoria(categorias):
    print("Selecione uma categoria de produto:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    escolha = int(input("Digite o número da categoria desejada: "))
    return categorias[escolha - 1]

def cadastrar_produto(produtos):
    ultimo_id = len(produtos)
    while True:
        id_produto = gerar_id(ultimo_id)
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
        ultimo_id += 1
    return produtos

def alterar_produto(produtos):
    imprimir_produtos(produtos)
    while True:
        produtos[id_produto] = {
            'nome': input('Digite o nome do produto: '),
            'categorias': selecionar_categoria(['Informática', 'Roupas', 'Papelaria', 'Livros', 'Brinquedos']),
            'preco': float(input('Digite o preço do produto: ')),
            'quantidade_estoque': int(input('Digite a quantidade do produto: ')),
            'descricao': input('Digite uma breve descrição do produto: ')
        }
        continuar = input("Deseja alterar outro produto? (s/n): ").strip().lower()
        if continuar != 's':
            break
        ultimo_id += 1
    return produtos


def imprimir_produtos(produtos):
    for chave, dados_produto in produtos.items():
        print(f'ID: {chave}')
        for campo, valor in dados_produto.items():
            print(f'  {campo.capitalize()}: {valor}')
        print('-' * 30)


