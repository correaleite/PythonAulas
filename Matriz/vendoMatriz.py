matriz = [[1,2,3], [4,5,6]]

x = len(matriz)
print(x)

y = len(matriz[0])
print(y)
print()

for i in range(x):
    for j in range(y):
        print(matriz[i][j], end="\t")
    print()
