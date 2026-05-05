
'''
#funções min() & max() montadas
lista = [3,10,7,8,1,9,8,5,8]

menor = lista[0]
maior = lista[0]

for num in lista:
    if menor > num:
        menor = num
    if maior < num:
        maior = num

print(f'O menor valor da lista é {menor}\n')
print(f'O menor valor da lista é {maior}\n')
'''
#função sort() montada
lista = [3,10,7,8,1,9,8,5,8]

for i in range(len(lista)):
    for j in range(len(lista)):
        if  lista[i]  < lista[j]:
            x = lista[i]
            lista[i] = lista[j]
            lista[j] = x
            
print(lista)



