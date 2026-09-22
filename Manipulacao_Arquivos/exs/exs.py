# # EX1
# with open('arquivoEx1.txt', 'w', encoding='utf-8') as arquivo:
#     for item in range(10):
#         n = int(input("Digite um número: "))
#         arquivo.write(f" {n}\n")

# arquivo.close()

# # EX2
# total = 0
# with open('arquivoEx1.txt', 'r', encoding='utf-8') as arquivo:
#     for item in arquivo:
#         total += int(item)
#     print(f"soma: {total}")

# arquivo.close()

# # EX3
# with open('arquivoEx1.txt', 'w', encoding='utf-8') as arquivo:
#     n = int(input("Digite um número: "))
#     while n != "0":
#         n = input("Digite um caracter: ")
#         print("(Digite 0 para sair)")
#         arquivo.write(f"{n}\n")

# arquivo.close()

# EX4
n = ''
while n != 0:
        n = int(input("Digite um número: "))
        print("(Digite 0 para sair)")
        if n == 0:
             print()
        if n % 2 == 0:
            with open('pares.txt', 'a', encoding='utf-8') as arquivoPares:
                 arquivoPares.write(f"{n}\n")
        else:
            with open('impares.txt', 'a', encoding='utf-8') as arquivoImpares:
                 arquivoImpares.write(f"{n}\n")
                 


# EX5
with open('arquivoPI.txt', 'w', encoding='utf-8') as arquivoPI:
     arquivoPares =  open('pares.txt', 'r', encoding='utf-8')
     arquivoImpares =  open('impares.txt', 'r', encoding='utf-8')
     juncao = arquivoPares.read() + arquivoImpares.read()
     arquivoPI.write(juncao)

    
arquivoPI.close()
