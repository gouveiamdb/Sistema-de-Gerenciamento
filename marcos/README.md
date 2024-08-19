# Sistema de Gerenciamento de Inventário para Loja Virtual

## 1- Descrição

Este repositório contém o código-fonte do projeto de desenvolvimento de um **Sistema de Gerenciamento de Inventário** para uma loja virtual. O sistema permite o cadastro, atualização, exclusão e listagem de produtos, além de gerenciar vendas e gerar relatórios detalhados em formato CSV.

## Objetivo

O objetivo deste projeto é construir um sistema robusto e eficiente, capaz de lidar com erros de forma elegante, enquanto oferece funcionalidades completas para o gerenciamento de inventário.

## Funcionalidades

- **Cadastro de Produtos**: Adicionar novos produtos ao inventário.
- **Atualização de Produtos**: Modificar as informações de produtos existentes.
- **Exclusão de Produtos**: Remover produtos do inventário.
- **Listagem de Produtos**: Visualizar todos os produtos cadastrados.
- **Gestão de Vendas**: Registrar e processar vendas de produtos.
- **Geração de Relatórios**: Gerar relatórios detalhados em formato CSV sobre o estoque e vendas.

## Requisitos
Python 3.x
Nenhuma biblioteca externa adicional é necessária.

## Como Rodar o Projeto
1- Clone o repositório ou baixe os arquivos do projeto.
2- Navegue até a pasta do projeto em seu terminal.
3- Execute o arquivo main.py
**python main.py**
4- O menu interativo será exibido no terminal, e você poderá navegar pelas opções

# 2- Documentação das Funções

## arquivo_csv.py

### `criar_arquivo_csv(nome_arquivo='relatorio_estoque.csv')`

Cria um arquivo CSV com cabeçalho, se ele ainda não existir.  
**Parâmetro:**  
`nome_arquivo` - Nome do arquivo CSV a ser criado (default: `relatorio_estoque.csv`).

### `carregar_produtos(nome_arquivo='relatorio_estoque.csv')`

Carrega os produtos do arquivo CSV e retorna um dicionário de produtos.  
**Parâmetro:**  
`nome_arquivo` - Nome do arquivo CSV a ser lido (default: `relatorio_estoque.csv`).  
**Retorno:**  
Um dicionário onde a chave é o ID do produto e o valor é outro dicionário com os dados do produto.

### `salvar_produtos(produtos, nome_arquivo='relatorio_estoque.csv')`

Salva o dicionário de produtos no arquivo CSV.  
**Parâmetros:**  
`produtos` - Dicionário de produtos a ser salvo.  
`nome_arquivo` - Nome do arquivo CSV onde os dados serão salvos (default: `relatorio_estoque.csv`).

### `gerar_relatorio_csv(produtos, nome_arquivo='relatorio_estoque.csv')`

Gera um relatório CSV com os produtos cadastrados.  
**Parâmetros:**  
`produtos` - Dicionário de produtos a ser salvo.  
`nome_arquivo` - Nome do arquivo CSV onde os dados serão salvos (default: `relatorio_estoque.csv`).  
**Saída:**  
Mensagem informando que o relatório foi gerado.

## produto.py

### `gerar_id(produtos)`

Gera um novo ID para o produto, incrementando o último ID existente.  
**Parâmetro:**  
`produtos` - Dicionário de produtos.  
**Retorno:**  
String com o novo ID no formato de quatro dígitos.

### `selecionar_categoria(categorias)`

Exibe as categorias de produtos e solicita ao usuário a seleção de uma.  
**Parâmetro:**  
`categorias` - Lista de categorias disponíveis.  
**Retorno:**  
Categoria selecionada pelo usuário.

### `cadastrar_produto(produtos)`

Solicita informações do produto ao usuário e o adiciona ao dicionário de produtos.  
**Parâmetro:**  
`produtos` - Dicionário onde o novo produto será adicionado.

### `alterar_produto(produtos)`

Permite a alteração das informações de um produto existente.  
**Parâmetro:**  
`produtos` - Dicionário de produtos a ser atualizado.

### `imprimir_produtos(produtos)`

Exibe todos os produtos cadastrados com seus detalhes.  
**Parâmetro:**  
`produtos` - Dicionário de produtos a serem exibidos.

### `remover_produto(produtos)`

Remove um produto do dicionário de produtos.  
**Parâmetro:**  
`produtos` - Dicionário de produtos.

## menu.py

### `menu()`

Exibe o menu principal do sistema e conecta as funcionalidades.  
Carrega os produtos, exibe as opções do menu e chama as funções correspondentes conforme a escolha do usuário.

## 3- Exemplo de Uso
Ao executar o programa, o menu principal será exibido:
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
Digite o número da opção desejada e siga as instruções.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python

## Amostragem

## Autores

- **Giovanni Ornellas**  
  [GitHub](https://github.com/Giovanni-Ornellas) | [LinkedIn](https://www.linkedin.com/in/giovanni-ornellas-419610227/)

- **Matheus Gouveia**  
  [GitHub](https://github.com/gouveiamdb) | [LinkedIn](https://www.linkedin.com/in/matheus-gouveia-387a19258/)

- **Murilo Silva**  
  [GitHub](https://github.com/usuario3) | [LinkedIn](https://www.linkedin.com/in/murilo-silva-bb2741a1)

- **Marcos Carvalho**
[GitHub](https://github.com/MarcosFN2014) | [LinkedIn](https://www.linkedin.com/in/marcos-carvalho-8173a2241/)

