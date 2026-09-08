'''

Exe1 - Criar e manipular Sets()
Crie dois conjuntos (sets), um com números pares e outro com números ímpares. Os números devem variar de 1 a 10

Exe2 - Remover Duplicatas
Dada uma lista com alguns elementos duplicados, converta a lista em um set para remover duplicatas e depois converta de volta para a lista

Exe3 - Contar elementos únicos
Dada uma lista com vários eleemntos (alguns duplicados), crie um set a partir desta lista e conte a quantidade de elementos únicos

'''

# EX1
pares = {2, 10, 6, 4, 8}
impares = {1, 9, 3, 5, 7}
print(pares)
print(impares)

# EX2
pares = [2, 10, 6, 4, 2, 6]
conjunto = set(pares)
print(conjunto)
print(list(conjunto))

# EX3

pares = [2, 10, 6, 4, 2, 6]
conjunto = set(pares)
print(len(conjunto))
