# um arquivo chamado "arquivo.txt" será aberto para leitura
# arquivo = open('arquivo.txt', 'r')


# a função read() irá copiar todo o conteúdo do arquivo para uma string
# texto = arquivo.read()
# print(texto)

# # o for irá percorrer todo o arquivo linha por linha
# for linha in arquivo:
#     print(linha)

# fecha o arquivo e libera da memória
# arquivo.close()

# --------------------------------- w

# # aberto para escrita
# arquivo = open('arquivo.txt', 'w')

# arquivo.write("Este texto será escrito no arquivo\n")

# nome = input('Digite seu nome: ')
# arquivo.write(nome + "\n")

# idade = int(input('Digite sua idade: '))
# arquivo.write(str(idade) + "\n")

# fecha o arquivo e libera da memória
# arquivo.close()

# --------------------------------- a

# # aberto para adicionar conteudo
# arquivo = open('arquivo.txt', 'a')

# arquivo.write("Este texto será escrito no arquivo\n")

# fecha o arquivo e libera da memória
# arquivo.close()

with open('meuarquivo.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:  # percorre as linhas do arquivo
        print(linha)

print('Aqui o arquivo já está fechado. ')