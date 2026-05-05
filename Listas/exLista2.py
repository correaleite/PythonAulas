'''
#Ex1
import random
 
num = []

 
for i in range(1,9,1):
    n = random.randint(1,20)
    num.append(n)

print(num)
'''

'''
#Ex2
import random
numerosPares = []
numerosImpares = []
for i in range(1,29,1):
    n = random.randint(1,50)
    if n % 2:
        numerosImpares.append(n)
    else:
        numerosPares.append(n)
print(f'Números Pares:{numerosPares}')
print(f'Números ìmpares:{numerosImpares}')
'''

#Ex5

lista1 = [1,3,5,7,9,11,13,15,17,19]
lista2 = [2,4,6,8,10,12,14,16,18,20]
lista3 = lista1 + lista2

print(lista3)
