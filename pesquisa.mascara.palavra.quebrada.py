import re

# Definindo o padrão de busca
padrao = r'\bHHC\w*8I\b'

with open('log001.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Buscando e imprimindo todas as palavras que correspondem ao padrão
for i, linha in enumerate(linhas):
    correspondencias = re.findall(padrao, linha)
    if correspondencias:
        print(f'Linh: {i + 1}: {correspondencias}')
