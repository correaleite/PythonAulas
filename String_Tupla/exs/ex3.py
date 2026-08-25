def conta_vogais(texto):
    cont = 0
    vogais = 'aeiou'
    for caracter in texto:
        if caracter.lower() in vogais:
            cont += 1
    return cont

texto = input('Digite o Texto: ')
quantidade = conta_vogais(texto)
print(f'Quantidade de vogais: {quantidade}')
