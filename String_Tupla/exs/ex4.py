def lista_palavras(frase):
    sepador = frase.split(" ")
    return sepador

print('frase:')
frase = input('')

res = lista_palavras(frase)
print(res)
