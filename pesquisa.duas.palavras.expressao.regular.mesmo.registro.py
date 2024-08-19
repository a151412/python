import re

# Palavras a serem pesquisadas
palavra1 = "HHC00338I"
palavra2 = "IOA800"

# Definindo o padrão de busca (ordem independente)
padrao = rf'\b({palavra1}\b.*\b{palavra2})|\b({palavra2}\b.*\b{palavra1})'

with open('log001.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Buscando linhas que contenham ambas as palavras
for i, linha in enumerate(linhas):
    if re.search(padrao, linha):
        print(f'Linha {i + 1}: {linha.strip()}')
