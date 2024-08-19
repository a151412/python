# Procurando várias strings no arquivo
palavras = ['HHC02915I', 'HHC00811I', 'HHC01314I']

with open('log001.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i, linha in enumerate(linhas):
    for palavra in palavras:
        if palavra in linha:
            print(f'String "{palavra}" encontrada na linha {i + 1}: {linha.strip()}')
