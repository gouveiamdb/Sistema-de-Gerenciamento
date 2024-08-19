#este é o ponto de entrada do programa. Ele inicializa o arquivo CSV e chama o menu.
from src.menu import menu
from src.arquivo_csv import criar_arquivo_csv

# Inicializa o arquivo CSV e carrega os produtos
criar_arquivo_csv()
menu()
