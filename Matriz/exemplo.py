linhas = int(input('Quantidade de linhas: '))
colunas = int(input('Quantidade de colunas: '))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input('Número: '))
        linha.append(n)
    matriz.append(linha)  #Insere cada linha na matriz
print(matriz)
