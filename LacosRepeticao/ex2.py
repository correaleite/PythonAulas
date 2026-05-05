cont = 1
soma = 0

while cont <= 15:
    numero = int(input(f"Digite o {cont} número: "))
    if numero%2 != 0:
        soma += numero
    cont += 1

print(f"soma de todos ímpares é {soma}")