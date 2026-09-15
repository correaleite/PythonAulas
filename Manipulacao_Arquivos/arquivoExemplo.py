"""
arquivo = open ("exemplo.txt", "w", encoding="utf-8")

arquivo.write("Olá. Esse é nosso primeiro arquivo\n")
arquivo.close()

arquivo = open ("exemplo.txt", "r", encoding='utf-8')

for linha in arquivo:
    print(linha)

arquivo.close()
"""
with open("exemplo.txt", "a", encoding="utf-8" ) as arquivo:
    arquivo.write("Esse texto deve aparecer no final do arquivo.\n")
    arquivo.write("Esse novo texto estará grudado no anterior.\n")