#estao todas as funcoes relacionadas ao arquivo CSV.
import csv

def criar_arquivo_csv(nome_arquivo='relatorio_estoque.csv'):
    try:
        with open(nome_arquivo, mode='x', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')
            escritor_csv.writerow(['ID', 'Nome', 'Categoria', 'Preço', 'Quantidade', 'Descrição'])
    except FileExistsError:
        pass # não faz nada se o arquivo ja existe

def carregar_produtos(nome_arquivo='relatorio_estoque.csv'):
    produtos = {}
    try:
        with open(nome_arquivo, mode='r', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=';')
            next(leitor_csv)  # pula o cabecalho
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
    except FileNotFoundError:
        criar_arquivo_csv(nome_arquivo)
    return produtos

def salvar_produtos(produtos, nome_arquivo='relatorio_estoque.csv'):
    with open(nome_arquivo, mode='a', newline='') as arquivo_csv:
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

def gerar_relatorio_csv(produtos, nome_arquivo='relatorio_estoque.csv'):
    salvar_produtos(produtos, nome_arquivo)
    print(f'Relatório gerado e salvo como {nome_arquivo}')
