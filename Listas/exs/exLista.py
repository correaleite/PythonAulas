#Ex1
'''
numerosPares = []
numerosImpares = []
for i in range(10):
    n = int(input('Informe um Número: '))
    if n % 2:
        numerosImpares.append(n)
    else:
        numerosPares.append(n)
print(f'Números Pares:{numerosPares}')
print(f'Números ìmpares:{numerosImpares}')
'''

#Ex2
'''
numeros = []
pares = []
soma = 0
somaPar = 0

for i in range(10):
    n = int(input('Informe um Número: '))
    soma += n
    numeros.append(soma)
    if n % 2 == 0:
        somaPar += n
        pares.append(somaPar)
    
print(f'Média aritmétrica: {soma/10}')
print(f'Soma dos Pares: {somaPar}')
'''

'''
#Ex3
import random
 
num = []
soma = 0
 
for i in range(1,21,1):
    n = random.randint(1,50)
    num.append(n)
    soma += n
 
print(f'Lista dos números sorteados são {num}')
print(f'Soma de todos os números é {soma}')
print(f'O menor número da lista é {min(num)}')
print(f'O maior número da lista é {max(num)}')
'''

'''
#Ex4
nomes = []
idades = []
ni = []

for i in range(10):
    nome = input(f'Informe o nome {i + 1}: ')
    nomes.append(nome)
    idade = int(input(f'Informe a idade {i + 1}: '))
    idades.append(idade)
    nomeIdade = nome
    if idade >= 18:
        ni.append(nomeIdade)
print(nomes)
print(idades)
print(ni)
'''

#Ex5
import random
 
num = []
 
for i in range(1,9,1):
    n = random.randint(1,50)
    num.append(n)

print(num)
numQuantidade = int(input('Ver quantidade do número: '))
print(f'Quantidade de {numQuantidade} na lista: {num.count(numQuantidade)}')
 

    




            








   
