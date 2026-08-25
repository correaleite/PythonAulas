def lista_palavras(frase):
    sepador = frase.split(" ")
    contador = len(sepador)
    return contador

print('frase:')
frase = input('')

res = lista_palavras(frase)
print(res)
