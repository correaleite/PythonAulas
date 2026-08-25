
def numeros(lista):
    lista = []
    cont = 1
    while cont < 11:
        numero = int(input(f"Digite o {cont} número: "))
        lista.append(numero)
        cont += 1
    return lista

a = numeros([])
print(a)