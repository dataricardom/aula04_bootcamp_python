import csv

caminho_arquivo_path: str = "exemplo.csv"

arquivo_csv: list = []

with open(caminho_arquivo_path, mode='r', encoding= 'utf-8') as arquivo:

    # Cria um objeto leitor de csv
    leitor_csv = csv.DictReader(arquivo)

    #Convertendo

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)