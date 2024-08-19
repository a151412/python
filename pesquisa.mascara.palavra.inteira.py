import re

# Usando uma expressão regular para encontrar padrões
padrao = r'\bHHC01314I\b'  # Encontra a palavra "Python" como uma palavra inteira

with open('log001.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i, linha in enumerate(linhas):
    if re.search(padrao, linha):
        print(f'Padrão "{padrao}" encontrado na linha {i + 1}: {linha.strip()}')
