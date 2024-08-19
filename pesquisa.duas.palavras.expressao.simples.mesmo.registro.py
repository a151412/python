# Palavras a serem pesquisadas
palavra1 = "HHC00338I"
palavra2 = "IOA800"

with open('log001.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Buscando linhas que contenham ambas as palavras (ordem independente)
for i, linha in enumerate(linhas):
    if palavra1 in linha and palavra2 in linha:
        print(f'Linha {i + 1}: {linha.strip()}')
