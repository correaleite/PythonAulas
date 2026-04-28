lista = []

type(lista)

list

lista = ['Maelle', 3, 3.6]
print(lista)

lista = [2,3,[5,5]]

n = 4 + 5
lista = [n,5]
print(lista)

lista = ['KIDinho', 'Verso', 'Melínoe', 'Ryu', 'Redshell']

print(lista[1])

print(len(lista))

lista.append('Correaleite')
print(lista)

lista.insert(2,'Maelle')
print(lista)

lista.pop(0)
print(lista)

for item in lista:
    print(item)

numeros = []
for i in range(5):
    n = int(input('Informe um Número: '))
    numeros.append(n)
print(numeros)

numeros1 = []
while True:
    n1 = int(input('Informe um Número: '))
    if n1 == 0:
        break
    numeros1.append(n1)
print(numeros1)