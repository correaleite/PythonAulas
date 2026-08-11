import random
    
def preencher_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(1,20))
        matriz.append(linha)
    return matriz
       
def exibir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()

def diagonal_principal(matriz):
    total = 0
    i = 0
    j = 0
    while i < len(matriz):
        total += matriz[i][j]
        i += 1
        j += 1
    return total

def menor_numero(matriz, linhas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            print(linha)

    menor = min(linha)

    return menor

        



#Main
linhas = 5
colunas = 5
m = []
m = preencher_matriz(linhas, colunas)

exibir_matriz(m)
print(f"O somatório dos valores da "
      f"diagonal principal dessa matriz é: "
      f"{diagonal_principal(m)} "
      f"{menor_numero(m, linhas)}")
