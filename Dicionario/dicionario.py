# dicionario = { 'name': 'Bob',
#               'age': 25,
#               'job': 'Dev',
#               'city': 'New York',
#               'email': 'Bob@web.com'}

# # Atualizar item
# dicionario['job'] = 'Manager'  # altera o valor associado a chave

# print(dicionario)
# print(dicionario['name'])

# dicionario['gender'] = 'non-binary'  # Inserir novo item
# print(dicionario)

# # Criar chave com valor
# info = input("nova chave: ")
# valor = input("valor da chave: ")
# dicionario[info] = valor
# print(dicionario)

# # Remover itens
# dicionario.pop('city')
# print(dicionario)

# #Buscar itens
# for n in dicionario.keys():
#     print(n) # exibe todas chaves do dicionario

# for n in dicionario.values():
#     print(n) # exibe todos valores das chaves do dicionario

# for chave, valor in dicionario.items():
#     print(chave,valor) # exibe todos items do dicionario

# # verifica se o item existe no dicionario
# if 'likes' in dicionario:
#     print('A chave existe no dicionario')
# else:
#     print('a chave não existe no dicionario')

# # Exemplo de busca
# alunos = {}

# for n in range(5):
#     ra = input('Informe o RA:')
#     nome = input('Informe o nome:')
#     alunos[ra] = nome

# print(alunos)

# notas = {'190': [8, 7.5, 5, 10],
#          '263': [2, 9.2, 7.9, 8.3],
#          '128': [6, 3, 5, 7]}

# print(notas['190'])
# print(notas['190'][0])

# # Outro Exemplo
aluno = {}

for i in range(5):
    rm = input("Informe o RM: ")
    notas = []
    for j in range(6):
        n = float(input("Insira a nota: "))
        notas.append(n)
    aluno[rm] = notas

print(aluno)

# # Exemplo loja
clientes = {1234: {'nome': 'João', 'idade': 24},
            5635: {'nome': 'Paula', 'idade': 34},
            9212: {'nome': 'Lucas', 'idade': 27},}

print(clientes[5635]['nome'])
print(clientes[5635]['idade'])