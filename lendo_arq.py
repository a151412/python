# Abrindo e lendo o conteúdo de um arquivo
with open('log001.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)
