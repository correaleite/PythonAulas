def removedor_espaco(texto):
    removedor = texto.replace(" ", "")
    return removedor

print('frase:')
frase = input('')

res = removedor_espaco(frase)
print(f'Sem espaço:{res}')
