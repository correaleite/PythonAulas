# Estrutura de Dados (coleção de dados)
# Definidas entre chaves {}
# Estrutura não ordenada e não indexada
conjunto = {"maçã", "banana", "manga", "banana"}
print(conjunto)

# Conjuntos são heterogêneos
conjunto = {"FIAP", 34, 5.6, "abc", True, 2, 2}
print(conjunto)

# Tamanho do Conjunto
print(len(conjunto))

# Acessando elementos do conjunto
print(34 in conjunto)
print(35 in conjunto)

# for item in conjunto:
#     print(item)

# Inserindo itens ao conjunto
# add()

nomes = {"Ryu", "Yasmin", "Mirella"}
nomes.add("Stalin")
print(nomes)

# Removendo um elemento no conjunto
# remove() | discard()

nomes.remove("Yasmin")
print(nomes)
# Discard não da erro
nomes.discard("Allen")
print(nomes)

#Preenchendo conjuntos com input()
# numeros = set()
# print(numeros)
# for i in range(5):
#     n = int(input('Número: '))
#     numeros.add(n)
# print(numeros)

# Método intersection 
x = {"Louco", "Feliz", "Triste"}
y = {"Nuvem", "Feliz", "Sol"}
z = x.intersection(y)
print(z)

# Differecence
z = x.difference(y)
print(z)
