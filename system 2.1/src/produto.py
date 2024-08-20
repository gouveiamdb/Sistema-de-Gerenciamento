from src.arquivo_csv import salvar_produtos

#funcoes relacionadas a manipulacao de produtos.
def gerar_id(produtos):
    #Gera um ID único para o produto baseado no número total de produtos.
    if produtos:
        return str(max(int(id_produto) for id_produto in produtos.keys()) + 1)
    return '1'

def selecionar_categoria(categorias):
    print("Selecione uma categoria de produto:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    escolha = int(input("Digite o número da categoria desejada: "))
    return categorias[escolha - 1]   

def cadastrar_produto(produtos):
    while True:
        id_produto = gerar_id(produtos)
        
        while True:
            nome_produto = input('Digite o nome do produto: ')
            if nome_produto.strip().isalpha():
                break
            else:
                print("Por favor, insira um nome válido (somente letras).")
        
        while True:
            try:
                categoria_num = int(input('''Selecione uma categoria 
    1-Informática 
    2-Roupas 
    3-Papelaria 
    4-Livros 
    5-Brinquedos 
    '''))
                if 1 <= categoria_num <= 5:
                    categorias = ['Informática', 'Roupas', 'Papelaria', 'Livros', 'Brinquedos']
                    categoria_produto = categorias[categoria_num - 1]
                    break
                else:
                    print("Por favor, selecione um número entre 1 e 5.")
            except ValueError:
                print("Por favor, insira um número válido para a categoria.")
        
        while True:
            try:
                preco_produto = float(input('Digite o preço do produto: '))
                break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o preço.")
        
        while True:
            try:
                quantidade_estoque = int(input('Digite a quantidade do produto: '))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido para a quantidade.")
        
        descricao_produto = input('Digite uma breve descrição do produto: ')
        
        produtos[id_produto] = {
            'nome': nome_produto,
            'categorias': categoria_produto,
            'preco': preco_produto,
            'quantidade_estoque': quantidade_estoque,
            'descricao': descricao_produto
        }
        
        salvar_produtos(produtos)
        confirmar = input("Adicionar novo produto? (s/n): ").strip().lower()
        if confirmar != 's':
            break 

def alterar_produto(produtos):
    imprimir_produtos(produtos)
    id_produto = input('Digite o ID do produto que deseja alterar: ')
    if id_produto in produtos:
        print(f'Produto escolhido: {produtos[id_produto]}')
        print('''O que deseja atualizar? 
        1 - Nome
        2 - Categoria
        3 - Preço
        4 - Quantidade
        5 - Descrição
        6 - Todas as informações
        ''')
        sub_opcao = input('Escolha uma opção acima: ')
        if sub_opcao == '1':
            produtos[id_produto]['nome'] = input('Digite o novo nome: ')
        elif sub_opcao == '2':
            categorias = ['Informática', 'Roupas', 'Papelaria', 'Livros', 'Brinquedos']
            produtos[id_produto]['categorias'] = selecionar_categoria(categorias)
        elif sub_opcao == '3':
            produtos[id_produto]['preco'] = float(input('Digite o novo preço: '))
        elif sub_opcao == '4':
            produtos[id_produto]['quantidade_estoque'] = int(input('Digite a nova quantidade: '))
        elif sub_opcao == '5':
            produtos[id_produto]['descricao'] = input('Digite a nova descrição: ')
        elif sub_opcao == '6':
            produtos[id_produto]['nome'] = input('Digite o novo nome: ')
            categorias = ['Informática', 'Roupas', 'Papelaria', 'Livros', 'Brinquedos']
            produtos[id_produto]['categorias'] = selecionar_categoria(categorias)
            produtos[id_produto]['preco'] = float(input('Digite o novo preço: '))
            produtos[id_produto]['quantidade_estoque'] = int(input('Digite a nova quantidade: '))
            produtos[id_produto]['descricao'] = input('Digite a nova descrição: ')
        else:
            print('Opção inválida.')
        
        salvar_produtos(produtos)
    else:
        print('Produto não encontrado.')

def imprimir_produtos(produtos):
    for chave, dados_produto in produtos.items():
        print(f'ID: {chave}')
        for campo, valor in dados_produto.items():
            print(f'  {campo.capitalize()}: {valor}')
        print('-' * 30)        

def remover_produto(produtos):
    id_produto = input('Digite o ID do produto que deseja remover: ')
    if id_produto in produtos:
        produtos.pop(id_produto)
        salvar_produtos(produtos)
        print('Produto removido com sucesso.')
    else:
        print('Produto não encontrado.')