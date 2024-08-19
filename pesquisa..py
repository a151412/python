# Procurando uma string específica no arquivo
palavra = 'HHC01427I'

with open('log001.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i, linha in enumerate(linhas):
    if palavra in linha:
        print(f'String "{palavra}" encontrada na linha {i + 1}: {linha.strip()}')
