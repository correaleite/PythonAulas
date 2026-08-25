# Sequencia de itens
# Estrutura imutável
# Pode conter diferentes tipos de dados

tupla = (2, 'abc', 4.5, 4)
print(tupla)

# conversão para uma lista
tupla = (4, 6, 2, 9)
lista = list(tupla)
print(lista)

# conversão para uma tupla
lista = [4, 6, 2, 9]
tupla = tuple(lista)
print(tupla)


def somar(a,b):
    return a+b, a*b

x = somar(2,3)
print(x)

y = list(x)
y[0] = 10
print(y)